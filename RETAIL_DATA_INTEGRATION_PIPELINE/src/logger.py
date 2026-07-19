import logging

from config.config import LOG_DIR


def setup_logging():

    LOG_DIR.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=LOG_DIR / "app.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    return logging.getLogger(__name__)