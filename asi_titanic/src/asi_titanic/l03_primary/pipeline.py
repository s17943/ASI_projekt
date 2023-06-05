from kedro.pipeline import Pipeline, node, pipeline

from asi_titanic.l03_primary.spine import create_spine


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_spine,
                inputs=["titanic", "params:spine_cols"],
                outputs="prm_spine",
                name="prm_spine",
            )
        ]
    )
