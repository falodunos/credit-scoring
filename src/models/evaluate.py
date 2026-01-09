"""Evaluation utilities."""
from sklearn.metrics import accuracy_score


def evaluate_model(model, X, y):
    preds = model.predict(X)
    return {"accuracy": accuracy_score(y, preds)}
