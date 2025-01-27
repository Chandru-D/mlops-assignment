"""Hyper-parameter tuning using GridSearchCV"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

# data = load_digits()
CSV_URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(CSV_URL, sep=";")
X = data.drop(["quality"], axis=1)  # Features
y = data["quality"]  # Labels

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}
model = RandomForestClassifier()
grid_search = GridSearchCV(model, param_grid, scoring='accuracy', cv=5, verbose=2)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)
