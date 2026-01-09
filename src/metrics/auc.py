"""AUC metric wrapper."""
from sklearn.metrics import roc_auc_score


def auc_score(y_true, y_prob):
    return roc_auc_score(y_true, y_prob)
