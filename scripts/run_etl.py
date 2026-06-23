import logging
import os
import time
from src.extract.extract import extract
from src.transform import transform

def log_tools():
    os.makedirs('logs', exist_ok=True)
    os.makedirs('data/extract', exist_ok=True)
    os.makedirs('data/transform', exist_ok=True)
    os.makedirs('data/load', exist_ok=True)
    datetime = time.strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(filename=f'logs/{datetime}.log', level=logging.INFO)


def main():
    # Open existing logging in a separate bash terminal for monitoring
    # tail -f logs/{datetime}.log
    logging.info("Running ETL process...")
    # Extract function returns a list of dataframes
    raw_data = extract()
    # Temporarily save raw data to CSV files for exploring in Jupyter notebooks
    for i, df in enumerate(raw_data):
        df.to_csv(f'data/extract/raw_data_part_{i}.csv', index=False)
    logging.info("Data extraction completed and saved to CSV files.")
    # Transform function processes the list of dataframes and returns a single cleaned and combined dataframe
    clean_df = transform.main(raw_data)
    clean_df.to_csv('data/transform/clean_data.csv', index=False)
    logging.info("Data transformation completed.")
    # Load function to save the cleaned data to a database or file
    # Currently not implemented as unnecessary for the project
    # load_data(clean_df)
    logging.info("Data loading completed.")
    logging.info("ETL process completed.")
    logging.shutdown()


if __name__ == '__main__':
    try:
        log_tools()
    except Exception as e:
        print(f"Error: {e}\nFailed to create logging tools\nClosing program")
        exit(1)
    try:
        main()
    except Exception as e:
        logging.error(f"ETL process failed: {e}")
        logging.shutdown()
        exit(1)
