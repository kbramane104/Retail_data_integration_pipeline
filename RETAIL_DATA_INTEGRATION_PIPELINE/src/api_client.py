import pandas as pd
import requests

from config.config import TIMEOUT

logger = __import__("logging").getLogger(__name__)


def fetch_data(url):

    try:

        response = requests.get(
            url,
            timeout=TIMEOUT,
            headers={
                "User-Agent": "Retail Data Integration Pipeline"
            },
        )

        response.raise_for_status()

        logger.info(f"Fetched {url}")

        return pd.json_normalize(response.json())

    except requests.RequestException as error:

        logger.error(error)

        return pd.DataFrame()