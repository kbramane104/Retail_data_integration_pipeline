from config.config import ENDPOINTS

from src.logger import setup_logging
from src.report_generator import generate_report
from src.pipeline import process_dataset


def main():

    setup_logging()

    print("\nRetail Data Integration Pipeline\n")

    summary = []

    for dataset, url in ENDPOINTS.items():

        result = process_dataset(dataset, url)

        if result:

            summary.append(result)

    report = generate_report(summary)

    print(report)

    print("\nCompleted Successfully")


if __name__ == "__main__":

    main()