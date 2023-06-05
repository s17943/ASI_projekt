from kedro.pipeline import Pipeline, node, pipeline

from asi_titanic.l05_model_input.master import build_master_table


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=build_master_table,
                inputs=[
                    "prm_spine",
                    "params:spine_cols",
                    "ftr_family_size",
                    "ftr_title",
                    "ftr_others",
                ],
                outputs="master",
                name="master",
            )
        ]
    )
