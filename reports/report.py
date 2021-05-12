import os
import inspect
import logging.config
import webbrowser

import yaml
import pandas as pd
from pandas_profiling import ProfileReport

# logging
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
main_dir = os.path.dirname(current_dir)
logger = logging.getLogger("PIPELINE")
with open(os.path.join(main_dir, "configs", "logging_config.yaml")) as config_fin:
    logging.config.dictConfig(yaml.load(config_fin.read(), Loader=yaml.FullLoader))


def main():
    logger.info("EDA report preparation started")
    source_df = pd.read_csv(os.path.join(main_dir, "data", "raw", "heart.csv"))

    # report
    profile = ProfileReport(source_df)
    report_path = os.path.join(main_dir, "reports", "EDA_report.html")
    profile.to_file(output_file=report_path)
    webbrowser.open(f"file:///{report_path}", new=2)
    logger.info("EDA report preparation completed")


if __name__ == "__main__":
    main()