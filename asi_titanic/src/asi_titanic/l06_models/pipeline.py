from kedro.pipeline import Pipeline, node, pipeline

from asi_titanic.l06_models.build_model import build_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=build_model,
                inputs=["master", "params:model_params"],
                outputs="best_estimator",
                name="best_estimator",
            )
        ]
    )
