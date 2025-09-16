from src.extract import extract_data, extract_forces, extract_dates, call_limit
import logging
import time

# Retrieve logger instance from main ETL script
logger = logging.getLogger(__name__)


# Main function to run the extraction process
# Includes logging for monitoring and debugging
def extract():
    logger.info("Applying rate limiting to avoid API throttling...")
    call_limit.check_rate()
    logger.info("Retrieving base API URL...")
    api = call_limit.base_api
    logger.info("Beginning timer for extraction process...")
    start_timer = time.time()
    logger.info("Starting the extraction process...")
    logger.info("Extracting force data from the UK Police API...")
    forces_df = extract_forces.extract_forces(api)
    logger.info("Extracting date data from the UK Police API...")
    dates_df = extract_dates.extract_dates(api)
    logger.info("Extracting crime data from the UK Police API...")
    crime_data_df = extract_data.extract_data(api, forces_df, dates_df)
    logger.info("Extraction process completed.")
    end_timer = time.time()
    elapsed_time = end_timer - start_timer
    logger.info(f"Total extraction time: {elapsed_time:.2f} seconds")
    logger.info("Outputting dataframes...")
    return [forces_df, dates_df, crime_data_df]


if __name__ == "__main__":
    extract()
