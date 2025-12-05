# data_cleaning.py
# Helper functions for cleaning SpaceX datasets used in the capstone project.

import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Load CSV into DataFrame."""
    return pd.read_csv(path)

def drop_unused_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Drop a list of columns if they exist."""
    return df.drop(columns=[c for c in cols if c in df.columns], errors='ignore')

def fill_missing_with_mode(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Fill missing values in specified columns with the column mode."""
    for col in columns:
        if col in df.columns:
            mode_val = df[col].mode(dropna=True)
            if not mode_val.empty:
                df[col].fillna(mode_val.iloc[0], inplace=True)
    return df

def save_csv(df: pd.DataFrame, path: str) -> None:
    """Save DataFrame to CSV."""
    df.to_csv(path, index=False)
