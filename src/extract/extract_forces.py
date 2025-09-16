from src.extract.extract_request import extract_request
from src.extract import call_limit
import pandas as pd
import logging


# Retrieve logger instance from main ETL script
logger = logging.getLogger(__name__)


# Function to extract force data from the UK Police API
def extract_forces(api):
    logger.info("Extracting force data from the UK Police API...")
    response = extract_request(api + "forces")
    forces_data = response.json()
    logger.info("Converting force data to DataFrame...")
    forces_df = pd.DataFrame(forces_data)
    logger.info("Force data extraction completed.")
    return forces_df


if __name__ == "__main__":
    extract_forces(call_limit.base_api)
