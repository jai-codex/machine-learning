import pandas as pd
import joblib

model = joblib.load("house_price_model.pkl")

def predict_house_price(
    med_inc,
    house_age,
    ave_rooms,
    ave_bedrms,
    population,
    ave_occup,
    latitude,
    longitude
):
    new_house = pd.DataFrame([{
        "MedInc" : med_inc,
        "HouseAge" : house_age,
        "AveRooms" : ave_rooms,
        "AveBedrms" : ave_bedrms,
        "Population" : population,
        "AveOccup" : ave_occup,
        "Latitude" : latitude,
        "Longitude" : longitude
    }])
    prediction = model.predict(new_house)
    price = prediction[0] * 100000
    return price

price = predict_house_price(
    5.0,
    20.0,
    6.0,
    1.0,
    1000.0,
    3.0,
    34.0,
    -118.0
)

print("Predicted house price: $", price)
