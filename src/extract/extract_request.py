import requests
import logging
import time

# Retrieve logger instance from main ETL script
logger = logging.getLogger(__name__)


# Function to make a GET request to the provided URL
def extract_request(url):
    # Implementing a simple retry mechanism for robustness
    max_retries = 3
    for attempt in range(max_retries):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        logger.error(
            f"Request to {url} failed with status code {response.status_code}"
        )
        time.sleep(2 ** attempt)  # Exponential backoff
    raise ValueError("Bad Request")
