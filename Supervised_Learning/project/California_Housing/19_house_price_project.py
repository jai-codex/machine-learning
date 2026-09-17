from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()

print("Features:")
print(data.feature_names)

print("\nShape:")
print(data.data.shape)

print("\nTarget:")
print(data.target[:10])