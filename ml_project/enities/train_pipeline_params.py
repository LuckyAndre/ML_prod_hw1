import yaml
from marshmallow_dataclass import class_schema
from dataclasses import dataclass
from typing import Optional

from .split_params import SplittingParams
from .feature_params import FeatureParams
from .train_params import TrainingParams


@dataclass()
class TrainingPipelineParams:
    input_data_path: str
    report_data_path: Optional[str]
    output_model_path: str
    output_features_transformer_path: str
    output_metric_path: str
    splitting_params: SplittingParams
    feature_params: FeatureParams
    train_params: TrainingParams


TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)


def read_training_pipeline_params(path: str) -> TrainingPipelineParams:
    with open(path, "r") as input_stream:
        schema = TrainingPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
