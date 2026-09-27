from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("house_price_model.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    new_house = pd.DataFrame([data])

    prediction = model.predict(new_house)

    price = prediction[0] * 100000

    return jsonify({
        "predicted_price": price
    })


if __name__ == "__main__":
    app.run(debug=True)