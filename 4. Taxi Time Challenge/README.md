### Problem Statement: Taxi Trip Duration

#### Objective:
Your task is to build a machine learning model to predict the duration of taxi trips. The model should utilize the features provided in the dataset and accurately estimate the trip duration in seconds.

#### Dataset Details:
The dataset includes the following columns:

1. **id**: A unique identifier for each trip.
2. **vendor_id**: A code representing the vendor associated with the trip.
3. **pickup_datetime**: The date and time when the taxi meter was activated.
4. **dropoff_datetime**: The date and time when the taxi meter was deactivated.
5. **passenger_count**: The number of passengers in the vehicle.
6. **pickup_longitude**: The longitude of the pickup location.
7. **pickup_latitude**: The latitude of the pickup location.
8. **dropoff_longitude**: The longitude of the dropoff location.
9. **dropoff_latitude**: The latitude of the dropoff location.
10. **store_and_fwd_flag**: Indicates whether the trip record was temporarily stored in the vehicle's memory (Y=Yes, N=No).
11. **trip_duration**: The actual duration of the trip in seconds (target variable).

#### Evaluation:
Your model's performance will be evaluated using appropriate metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R². Be sure to document and justify your choices of evaluation metrics. Additionally, the code should be well-documented and structured to ensure clarity.