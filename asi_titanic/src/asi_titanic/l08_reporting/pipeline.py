from kedro.pipeline import Pipeline, node, pipeline

from asi_titanic.l08_reporting.reporting import save_shap_summary_plot


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=save_shap_summary_plot,
                inputs=["best_estimator", "master", "params:model_params"],
                outputs="shap_plot",
                name="shap_plot",
            )
        ]
    )
