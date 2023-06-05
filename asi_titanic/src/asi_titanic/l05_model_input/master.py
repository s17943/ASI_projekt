import pandas as pd


def build_master_table(
    prm_spine: pd.DataFrame, spine_cols: list, *feature_tables: pd.DataFrame
) -> pd.DataFrame:
    master = prm_spine.copy()
    for feature_table in feature_tables:
        master = master.merge(feature_table, on=spine_cols, how="left")

    return master
