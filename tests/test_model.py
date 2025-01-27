import joblib
import os
import numpy as np


def test_model():
    # Define the path to model.pkl relative to the tests folder
    model_path = os.path.join(os.path.dirname(__file__), '../model.pkl')
    # Ensure the file exists before loading
    # print(os.path.exists(model_path))
    assert os.path.exists(model_path), f"{model_path} does not exist!"
    # Load the model
    model = joblib.load(model_path)
    x = np.array([[7.4, 0.7, 0, 1.9, 0.076, 11, 34, 0.9978, 3.51, 0.56, 9.4]])
    x = x.reshape(-1, 11)
    # print(round(model.predict(x)[0], 1) == 5.6)
    # Perform the test
    assert round(model.predict(x)[0], 1) == 5.6
