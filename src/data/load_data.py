"""Data loading utilities."""
import pandas as pd
from pathlib import Path


def load_csv(path: str or Path) -> pd.DataFrame:
    """Load CSV into a DataFrame."""
    return pd.read_csv(path)


if __name__ == "__main__":
    print("Run load_csv from this module to load data")
