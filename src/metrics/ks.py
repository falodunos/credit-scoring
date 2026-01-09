"""Kolmogorov-Smirnov statistic for binary classification scores."""
import numpy as np


def ks_stat(y_true, y_prob):
    """Compute a simple KS statistic approximation."""
    # Sort by predicted probability
    order = np.argsort(y_prob)
    y_sorted = y_true[order]
    n = len(y_true)
    cum_pos = np.cumsum(y_sorted) / max(1, y_sorted.sum())
    cum_neg = np.cumsum(1 - y_sorted) / max(1, (n - y_sorted.sum()))
    return float(np.max(np.abs(cum_pos - cum_neg)))
