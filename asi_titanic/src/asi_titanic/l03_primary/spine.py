import pandas as pd


def create_spine(titanic: pd.DataFrame, spine_cols: list) -> pd.DataFrame:
    return titanic[spine_cols + ["Survived"]]
