import shap
from kedro.extras.datasets.pickle import PickleDataSet
import pandas as pd
from typing import Dict
import matplotlib.pyplot as plt


def save_shap_summary_plot(estimater: PickleDataSet, master: pd.DataFrame, model_params: Dict):
    X = master[model_params["features"]]
    explainer = shap.Explainer(estimater)
    shap_values = explainer(X)
    shap.plots.beeswarm(shap_values[:, :, 1], show=False)
    fig = plt.gcf()

    return fig

