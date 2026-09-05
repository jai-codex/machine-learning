from sklearn.preprocessing import LabelEncoder

data = ["Yes", "No", "Yes", "No"]

encoder = LabelEncoder()

encoded_data = encoder.fit_transform(data)

print(encoded_data)