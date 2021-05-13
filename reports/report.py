import sys
import logging
import webbrowser
import click

import pandas as pd
from pandas_profiling import ProfileReport

from ml_project.enities.train_pipeline_params import (
    TrainingPipelineParams,
    read_training_pipeline_params,
)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def make_report(params: TrainingPipelineParams):
    logger.info("EDA report preparation started")
    source_df = pd.read_csv(params.input_data_path)

    # report
    profile = ProfileReport(source_df)
    profile.to_file(output_file=params.report_data_path)
    webbrowser.open(f"file:///{params.report_data_path}", new=2)
    logger.info("EDA report preparation completed")


@click.command(name="make_report")
@click.argument("config_path")
def make_report_command(config_path: str):
    params = read_training_pipeline_params(config_path)
    make_report(params)


if __name__ == "__main__":
    make_report_command()