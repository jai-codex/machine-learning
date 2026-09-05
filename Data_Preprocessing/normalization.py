import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = np.array([
    [18, 20000],
    [20, 50000],
    [25, 100000]
])

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(data)

print(scaled_data)
