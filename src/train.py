import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
import os

# Sample Training Data
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Train Model
model = LinearRegression()
model.fit(X, y)

# Get the absolute path to the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Save model to the project root
model_path = os.path.join(project_root, 'model.pkl')
joblib.dump(model, model_path)

print(f"Model saved to {model_path}")

# from sklearn.linear_model import LinearRegression
# import numpy as np
# # Save Model
# import joblib

# # Sample Training Data
# X = np.array([[1], [2], [3], [4]])
# y = np.array([2, 4, 6, 8])

# # Train Model
# model = LinearRegression()
# model.fit(X, y)

# joblib.dump(model, 'model.pkl')
