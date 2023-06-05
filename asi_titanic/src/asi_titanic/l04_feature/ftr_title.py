import pandas as pd


def create_ftr_title(titanic: pd.DataFrame, threshold: int) -> pd.DataFrame:
    ftr_person_title = titanic[["PassengerId", "Name"]].copy()
    ftr_person_title["Title"] = (
        ftr_person_title["Name"]
        .str.split(", ", expand=True)[1]
        .str.split(".", expand=True)[0]
    )
    title_names = ftr_person_title["Title"].value_counts() < threshold
    ftr_person_title["Title"] = ftr_person_title["Title"].apply(
        lambda x: "Others" if title_names.loc[x] == True else x
    )
    ftr_person_title["Title"] = ftr_person_title["Title"].astype("category").cat.codes
    ftr_person_title.drop(columns="Name", inplace=True)
    return ftr_person_title
