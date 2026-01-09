"""Training routines."""
from sklearn.ensemble import RandomForestClassifier


def train_model(X, y, random_state=42):
    model = RandomForestClassifier(n_estimators=100, random_state=random_state)
    model.fit(X, y)
    return model
