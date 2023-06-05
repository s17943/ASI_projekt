import pandas as pd


def create_ftr_family_size(titanic: pd.DataFrame) -> pd.DataFrame:
    ftr_family_size = titanic[["PassengerId", "SibSp", "Parch"]].copy()
    ftr_family_size["FamilySize"] = ftr_family_size["SibSp"] + ftr_family_size["Parch"]
    return ftr_family_size
