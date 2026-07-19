from config.config import DATA_DIR

import logging

logger = logging.getLogger(__name__)


def save_csv(df, dataset):

    DATA_DIR.mkdir(exist_ok=True)

    file_path = DATA_DIR / f"{dataset}.csv"

    df.to_csv(file_path, index=False)

    logger.info(f"Saved {file_path}")