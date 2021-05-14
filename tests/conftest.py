import os

import pytest
from typing import List, Optional


@pytest.fixture()
def random_state():
    return 7


@pytest.fixture()
def dataset_size():
    return 300


@pytest.fixture()
def dataset_path():
    curdir = os.path.dirname(__file__)
    return os.path.join(curdir, "train_data_sample.csv")


@pytest.fixture()
def target_col():
    return "target"


@pytest.fixture()
def categorical_features_yes() -> List[str]:
    return ["categorical"]


@pytest.fixture()
def categorical_features_no() -> Optional[str]:
    return None


@pytest.fixture
def numerical_features_yes() -> List[str]:
    return [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal"
    ]


@pytest.fixture()
def numerical_features_no() -> Optional[str]:
    return None


@pytest.fixture()
def features_to_drop_no() -> Optional[str]:
    return None
