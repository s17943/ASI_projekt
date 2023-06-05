from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
from kedro.extras.datasets.pickle import PickleDataSet
from typing import Dict
import mlflow

def build_model(master: pd.DataFrame, params: Dict) -> PickleDataSet:
    features = params["features"]
    target = params["target"]
    param_dist = params["param_dist"]
    clf = RandomForestClassifier()
    X = master[features]
    y = master[target]
    grid_search = GridSearchCV(clf, param_grid=param_dist, scoring="accuracy")
    grid_search.fit(X, y)
    # Calculate metrics
    best_estimator = grid_search.best_estimator_
    predicted_labels = best_estimator.predict(X)
    accuracy = accuracy_score(y, predicted_labels)
    precision = precision_score(y, predicted_labels)
    recall = recall_score(y, predicted_labels)
    f1 = f1_score(y, predicted_labels)

    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1", f1)

    return grid_search.best_estimator_
