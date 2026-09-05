import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([
    [18, 20000],
    [20, 50000],
    [25, 100000]
])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print(scaled_data)