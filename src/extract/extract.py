from src.extract import extract_data, extract_forces, extract_dates, call_limit
import logging
import time

# Retrieve logger instance from main ETL script
logger = logging.getLogger(__name__)


# Main function to run the extraction process
# Includes logging for monitoring and debugging
def extract():
    # Apply rate limiting to avoid API throttling
    logger.info("Applying rate limiting to avoid API throttling...")
    call_limit.check_rate()
    # Retrieve base API URL from base_api module
    logger.info("Retrieving base API URL...")
    api = call_limit.base_api
    # Start timer for performance monitoring of extraction phase
    logger.info("Beginning timer for extraction process...")
    start_timer = time.time()
    # Extract data from the API
    logger.info("Starting the extraction process...")
    # Extract forces data of UK Police API
    logger.info("Extracting force data from the UK Police API...")
    forces_df = extract_forces.extract_forces(api)
    # Extract dates data of UK Police API
    logger.info("Extracting date data from the UK Police API...")
    dates_df = extract_dates.extract_dates(api)
    # Extract crime data of UK Police API using forces and dates dataframes
    logger.info("Extracting crime data from the UK Police API...")
    crime_data_df = extract_data.extract_data(api, forces_df, dates_df)
    # End timer and log elapsed time for extraction phase
    logger.info("Extraction process completed.")
    end_timer = time.time()
    # Convert elapsed time to minutes and seconds
    elapsed_time = end_timer - start_timer
    elapsed_minutes = elapsed_time // 60
    elapsed_seconds = elapsed_time % 60
    logger.info(f"Total extraction time: {elapsed_minutes:.0f} minutes and "
                f"{elapsed_seconds:.2f} seconds")
    # Output the resulting dataframes
    logger.info("Outputting dataframes...")
    return [forces_df, dates_df, crime_data_df]


if __name__ == "__main__":
    extract()
