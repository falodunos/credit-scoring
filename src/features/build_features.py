"""Feature engineering helpers."""
import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # example feature: sum of numeric columns
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    if num_cols:
        df['num_sum'] = df[num_cols].sum(axis=1)
    return df
