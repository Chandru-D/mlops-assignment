import joblib
import os

def test_model():
    # Define the path to model.pkl relative to the tests folder
    model_path = os.path.join(os.path.dirname(__file__), '../model.pkl')
    
    # Ensure the file exists before loading
    assert os.path.exists(model_path), f"{model_path} does not exist!"
    
    # Load the model
    model = joblib.load(model_path)
    
    # Perform the test
    assert model.predict([[5]])[0] == 10
