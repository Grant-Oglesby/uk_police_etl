import logging
import os
import time
from src.extract.extract import extract

os.makedirs('logs', exist_ok=True)
datetime = time.strftime('%Y-%m-%d_%H-%M-%S')
logging.basicConfig(filename=f'logs/{datetime}.log', level=logging.INFO)


def main():
    # Open existing logging in a separate terminal window for real-time
    # monitoring
    os.system(f'gnome-terminal -- bash -c "tail -f logs/{datetime}.log; '
              f'exec bash"')
    logging.info("Running ETL process...")
    # Here you would add the actual ETL logic
    # For example:
    raw_data = extract()
    # Temporarily save raw data to CSV files for exploring in Jupyter notebooks
    for i, df in enumerate(raw_data):
        df.to_csv(f'data/extract/raw_data_part_{i}.csv', index=False)
    logging.info("Data extraction completed and saved to CSV files.")
    # clean_df = transform_data(raw_data)
    logging.info("Data transformation completed.")
    # load_data(clean_df)
    logging.info("Data loading completed.")
    logging.info("ETL process completed.")
    logging.shutdown()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f"ETL process failed: {e}")
        logging.shutdown()
        exit(1)
