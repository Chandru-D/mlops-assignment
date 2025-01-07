from sklearn.linear_model import LinearRegression
import numpy as np
# Save Model
import joblib

# Sample Training Data
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Train Model
model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
