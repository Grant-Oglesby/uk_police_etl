from src.extract.extract_request import extract_request
from src.extract import call_limit
import pandas as pd
import logging

# Retrieve logger instance from main ETL script
logger = logging.getLogger(__name__)


# Function to extract date information from the UK Police API
def extract_dates(api):
    response = extract_request(
        api + "crimes-street-dates"
    )
    dates_data = response.json()
    logger.info("Date data extraction completed.")
    logger.info("Converting date data to DataFrame...")
    dates_df = pd.DataFrame(dates_data)
    return dates_df


if __name__ == "__main__":
    extract_dates(call_limit.base_api)
