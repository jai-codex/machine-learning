import pandas as pd
import joblib

# Load the saved model
model = joblib.load("house_price_model.pkl")

# New house data
new_house = pd.DataFrame([{
    "MedInc": 5.0,
    "HouseAge": 20.0,
    "AveRooms": 6.0,
    "AveBedrms": 1.0,
    "Population": 1000.0,
    "AveOccup": 3.0,
    "Latitude": 34.0,
    "Longitude": -118.0
}])

# Make prediction
prediction = model.predict(new_house)

print("Predicted value:", prediction[0])

# Convert to approximate dollars
price = prediction[0] * 100000

print("Approximate house price: $", price)