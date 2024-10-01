import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split

# Load input data
input_file = "traffic_data.txt"
data = pd.read_csv(
    input_file, header=None, names=["Day", "Time", "City", "In_Progress", "Vehicles"]
)

# Filter for records from London
data = data[data["City"] == "London"]

# Convert categorical data to numerical data
label_encoders = {}
for column in ["Day", "Time", "City", "In_Progress"]:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le  # Store the encoder for later use

# Define features and target variable
X = data[["Day", "Time", "City", "In_Progress"]]
y = data["Vehicles"]

# Split data into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=5
)

# Extremely Random Forests regressor
params = {"n_estimators": 100, "max_depth": 4, "random_state": 0}
regressor = ExtraTreesRegressor(**params)
regressor.fit(X_train, y_train)

# Compute the regressor performance on test data
y_pred = regressor.predict(X_test)
print("Mean absolute error:", round(mean_absolute_error(y_test, y_pred), 2))

# Testing encoding on a single data instance
test_datapoint = ["Wednesday", "00:50", "London", "no"]  # Updated to London
test_datapoint_encoded = []

for i, item in enumerate(test_datapoint):
    if item.isdigit():
        test_datapoint_encoded.append(int(test_datapoint[i]))
    else:
        # Use .transform() and get the first element to avoid the warning
        encoded_value = label_encoders[list(label_encoders.keys())[i]].transform(
            [test_datapoint[i]]
        )
        test_datapoint_encoded.append(encoded_value[0])  # Get the single encoded value

# Convert to DataFrame for prediction to keep feature names
test_datapoint_encoded_df = pd.DataFrame([test_datapoint_encoded], columns=X.columns)

# Predict the output for the test datapoint
predicted_traffic = int(
    regressor.predict(test_datapoint_encoded_df)[0]
)  # Safe to access the first element
print("Predicted traffic:", predicted_traffic)
