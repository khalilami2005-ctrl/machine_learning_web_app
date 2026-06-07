import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import fetch_openml
import joblib

print("Loading MNIST...")
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False, parser='pandas')
X = X / 255.0

print(f"Training on {X.shape[0]} samples...")
model = SGDClassifier(loss='log_loss', max_iter=20, random_state=42, verbose=1)
model.fit(X, y)

joblib.dump(model, 'mnist_sklearn.pkl')
print("Saved mnist_sklearn.pkl")
