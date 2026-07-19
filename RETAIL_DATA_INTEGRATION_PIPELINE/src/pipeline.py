from src.api_client import fetch_data
from src.validator import validate_data
from src.cleaner import clean_data
from src.transformer import transform_data
from src.file_handler import save_csv
from src.report_generator import build_summary


def process_dataset(dataset, url):

    df = fetch_data(url)

    if df.empty:

        return None

    validation = validate_data(df)

    df = clean_data(df)

    df = transform_data(df, dataset)

    save_csv(df, dataset)

    # print(
    #     f"{dataset:<12}"
    #     f" Records={validation['records']:<5}"
    #     f" Missing={validation['missing_values']:<3}"
    #     f" Duplicates={validation['duplicates']:<3}"
    # )

    return build_summary(dataset, validation)