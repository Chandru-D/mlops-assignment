"""Flask application to predict features"""
import joblib
import numpy as np
from flask import Flask, request

app = Flask(__name__)

with open('model/model.pkl', 'rb') as f:
    model = joblib.load(f)
    print(type(model))

@app.route('/predict', methods=['POST'])
def predict():
    """
    To predict features
    Request body sample- {"features": [[7.4, 0.7, 0, 1.9, 0.076, 11, 34, 0.9978, 3.51, 0.56, 9.4]]}
    Response - list of predicted values
    """
    data = request.get_json()
    features = data.get("features")
    X = np.array(features)
    X = X.reshape(-1, 11) 
    prediction = model.predict(X)
    return {'prediction': prediction.tolist()}

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    """
    Check status of application server
    """
    print("I am alive !!!!!!")
    return "I am alive !!!!!!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
