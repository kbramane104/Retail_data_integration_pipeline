import pandas as pd

from config.config import REPORT_DIR

import logging

logger = logging.getLogger(__name__)


def build_summary(dataset, validation):

    return {
        "Dataset": dataset,
        "Records": validation["records"],
        "Columns": validation["columns"],
        "Missing Values": validation["missing_values"],
        "Duplicates": validation["duplicates"],
    }


def generate_report(summary):

    REPORT_DIR.mkdir(exist_ok=True)

    report = pd.DataFrame(summary)

    output = REPORT_DIR / "summary.xlsx"

    with pd.ExcelWriter(output) as writer:

        report.to_excel(
            writer,
            sheet_name="Summary",
            index=False,
        )

    logger.info("Report Generated")

    return report