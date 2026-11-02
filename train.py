import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import joblib

X, y = make_classification(
    n_samples=100,
    n_features=4,
    random_state=42
)

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")