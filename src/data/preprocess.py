"""Simple preprocessing steps."""
import pandas as pd


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder preprocessing: drops NA and returns dtypes converted."""
    df = df.copy()
    df = df.dropna()
    # Example: ensure numeric columns are float
    for c in df.select_dtypes(include=['int64','float64']).columns:
        df[c] = df[c].astype(float)
    return df
