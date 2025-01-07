from sklearn.linear_model import LinearRegression
import numpy as np

# Sample Training Data
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
import joblib
joblib.dump(model, 'model.pkl')
