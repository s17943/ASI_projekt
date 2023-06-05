from kedro.pipeline import Pipeline, node, pipeline

from asi_titanic.l04_feature.ftr_family_size import create_ftr_family_size
from asi_titanic.l04_feature.ftr_title import create_ftr_title
from asi_titanic.l04_feature.ftr_others import create_ftr_others


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_ftr_family_size,
                inputs="titanic",
                outputs="ftr_family_size",
                name="ftr_family_size",
            ),
            node(
                func=create_ftr_title,
                inputs=["titanic", "params:threshold"],
                outputs="ftr_title",
                name="ftr_title",
            ),
            node(
                func=create_ftr_others,
                inputs="titanic",
                outputs="ftr_others",
                name="ftr_others",
            ),
        ]
    )
