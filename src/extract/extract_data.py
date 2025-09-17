from src.extract.extract_request import extract_request
import pandas as pd
import logging

# Retrieve logger instance from main ETL script
logger = logging.getLogger(__name__)


# Function to extract crime data from the UK Police API
def extract_data(api, forces_df, dates_df):
    logger.info("Extracting crime data from the UK Police API...")
    all_crime_data = []

    for _, force in forces_df.iterrows():
        force_id = force['id']
        logger.info(f"Processing force: {force_id}")
        for _, date in dates_df.iterrows():
            date_str = date['date']
            logger.info(f"Fetching data for date: {date_str}")
            endpoint = (
                f"{api}stops-force?"
                f"date={date_str}&"
                f"force={force_id}"
            )
            response = extract_request(endpoint)
            crimes = response.json()
            if crimes:
                all_crime_data.extend(
                    [
                        {"force_id": force_id, **crime}
                        for crime in crimes
                    ]
                )
            else:
                logger.info(
                    f"No data returned for force {force_id} on date {date_str}"
                )

    logger.info("Converting crime data to DataFrame...")
    crime_data_df = pd.DataFrame(all_crime_data)
    logger.info("Crime data extraction completed.")
    return crime_data_df
