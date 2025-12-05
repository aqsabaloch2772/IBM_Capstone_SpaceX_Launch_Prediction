# utils.py
# General helper utilities for the SpaceX Capstone Project.

import pandas as pd

def preview(df: pd.DataFrame, rows: int = 5):
    """Return the first N rows of a DataFrame."""
    return df.head(rows)

def summarize(df: pd.DataFrame):
    """Return basic summary statistics."""
    return df.describe(include='all')

def missing_values(df: pd.DataFrame):
    """Return a count of missing values per column."""
    return df.isna().sum()

def unique_counts(df: pd.DataFrame):
    """Return the number of unique values per column."""
    return df.nunique()
