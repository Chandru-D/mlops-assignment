import joblib


def test_model():
    model = joblib.load('../src/model.pkl')
    assert model.predict([[5]])[0] == 10
