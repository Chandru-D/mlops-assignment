import joblib

def test_model():
    model = joblib.load('model.pkl')
    assert model.predict([[5]])[0] == 10
    