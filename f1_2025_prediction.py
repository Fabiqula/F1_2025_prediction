import fastf1
import requests
import pandas as pd


def f1_data(year, round_number):
    """data using F1 API via FastF1"""
    try:

        quali = fastf1.get_session(year, round_number, 'Q')
        quali.load()

        results = quali.results[['DriverNumber', 'FullName', 'TeamName', 'Q1', 'Q2', 'Q3']]

        results = results.rename(columns={'FullName': 'Driver'})

        for col in ['Q1', 'Q2', 'Q3']:
            results[col + '_sec'] = results[col].apply(
                lambda x: x.total_seconds() if pd.notnull(x) else None
            )

        print("\nQualifying Results Structure:")
        print(results.head())

        return results
    except Exception as e:
        print(f"Error fetching data: {e}")
        print("DataFrame columns available:", quali.results.columns.tolist())
        return None


f1_data(2025, 3)
