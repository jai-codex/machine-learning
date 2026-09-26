import pandas as pd
import joblib

# Load trained model
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
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude
    }])

    prediction = model.predict(new_house)

    return prediction[0] * 100000


# Get information from user
med_inc = float(input("Enter median income: "))
house_age = float(input("Enter house age: "))
ave_rooms = float(input("Enter average rooms: "))
ave_bedrms = float(input("Enter average bedrooms: "))
population = float(input("Enter population: "))
ave_occup = float(input("Enter average occupancy: "))
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))


price = predict_house_price(
    med_inc,
    house_age,
    ave_rooms,
    ave_bedrms,
    population,
    ave_occup,
    latitude,
    longitude
)

print("Predicted house price: $", price)
