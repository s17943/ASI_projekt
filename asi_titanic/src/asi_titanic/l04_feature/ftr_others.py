import pandas as pd


def create_ftr_others(titanic: pd.DataFrame) -> pd.DataFrame:
    ftr_others = titanic[
        ["PassengerId", "Pclass", "Sex", "Age", "Fare", "Embarked"]
    ].copy()
    ftr_others["Age"].fillna(ftr_others["Age"].median(), inplace=True)
    ftr_others["Sex"] = (ftr_others["Sex"] == "male").astype("int")
    ftr_others["Embarked"] = ftr_others["Embarked"].astype("category").cat.codes
    return ftr_others
