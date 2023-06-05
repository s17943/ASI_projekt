"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from asi_titanic.l03_primary import pipeline as primary
from asi_titanic.l04_feature import pipeline as feature
from asi_titanic.l05_model_input import pipeline as model_input
from asi_titanic.l06_models import pipeline as models
from asi_titanic.l08_reporting import pipeline as reporting


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    primary_pipeline = primary.create_pipeline()
    feature_pipeline = feature.create_pipeline()
    model_input_pipeline = model_input.create_pipeline()
    models_pipeline = models.create_pipeline()
    reporting_pipeline = reporting.create_pipeline()
    return {
        "__default__": pipeline(
            [primary_pipeline, feature_pipeline, model_input_pipeline, models_pipeline, reporting_pipeline]
        ),
        "primary_pipeline": primary_pipeline,
        "feature_pipeline": feature_pipeline,
        "model_input_pipeline": model_input_pipeline,
        "models_pipeline": models_pipeline,
        "reporting_pipeline": reporting_pipeline,
    }
