"""
How to Use F1 Lap Time Predictions

`all_predictions` is a list with 6 predicted lap times for a driver in a race round, starting from Free Practice 2 (FP2) to the Fastest Race Lap. It starts with FP1 time from `results` and builds predictions step-by-step, where each prediction uses FP1 plus all earlier predictions. Use these to guess how fast a driver will go in practice, qualifying, or the race.

What's Included:
    - 0: FP2_LapTime - Predicted FP2 time, using only FP1_LapTime from `results`.
    - 1: FP3_LapTime - Predicted FP3 time, using FP1_LapTime and predicted FP2_LapTime.
    - 2: Q1 - Predicted Qualifying 1 time, using FP1_LapTime, predicted FP2_LapTime, and FP3_LapTime.
    - 3: Q2 - Predicted Qualifying 2 time, using FP1_LapTime, predicted FP2_LapTime, FP3_LapTime, and Q1.
    - 4: Q3 - Predicted Qualifying 3 time, using FP1_LapTime, predicted FP2_LapTime, FP3_LapTime, Q1, and Q2.
    - 5: FastestRaceLap - Predicted fastest race lap, using FP1_LapTime, predicted FP2_LapTime, FP3_LapTime, Q1, Q2, and Q3.

How to Use It:
When new session starts and we get only FP1 times (First practice session) we can predict all times base on thatone practice session: 
Just set the ROUND_FOR_PREDICTION global variable at the top, and run the script. You can acces the prediction by: all_predictions[0].
Then after next practice lap times FP2 are updated we redownload them (rerun whole script) and enter all_predictions[1]
This will use both known times FP1 and FP2 for prediction of FP3, as well as all other times.
The predictions will get more accurate with more acctual lap times.

    1. **Get a Prediction**:
        - Grab a time with the index: `all_predictions[0]` for FP2, `all_predictions[5]` for race lap, etc.
        - Example: `print(all_predictions[0])` shows the predicted FP2 time in seconds.

    2. **Add to Your Data**:
        - Put predictions into your `results` DataFrame (from `create_df`) to compare with real times or fill gaps.
        - Example:
            ```python
            results.loc[(results['Round'] == 1) & (results['DriverNumber'] == 44), 'FP2_LapTime'] = all_predictions[0]
            ```

    3. **What You Can Do**:
        - See if predictions match real lap times.
        - Guess where drivers will start the race using Q1, Q2, Q3 predictions.
        - Plan race strategies with the FastestRaceLap prediction.

Parameters:
    all_predictions (list): A list of 6 numbers (in seconds) for predicted FP2, FP3, Q1, Q2, Q3, and FastestRaceLap times.

Tips:
    - FP2 prediction only uses FP1 time. Then, FP3 uses FP1 and predicted FP2, Q1 uses FP1, FP2, FP3, and so on, building up to the race lap prediction.
    - Check that FP1_LapTime in `results` is correct, since all predictions start from it.
    - Times are in seconds, just like in `results`.
    - If a driver’s predictions look off, double-check FP1 data or run `handle_nan_times`.

    Examples below.
"""
