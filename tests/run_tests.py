import pytest
import logging
import time
import os
import sys

os.makedirs('logs', exist_ok=True)
datetime = time.strftime('%Y-%m-%d_%H-%M-%S')
logging.basicConfig(filename=f'logs/test_{datetime}.log', level=logging.INFO)


def main():
    # Discover and run all tests in the 'tests' directory
    logging.info("Starting test suite...")
    logging.info(f"Test run started at {datetime}")

    # Run pytest and capture the results
    # Currently running component tests only
    result = pytest.main(['tests/component_tests'])

    if result != 0:
        logging.error("Some tests failed.")
        logging.shutdown()
        exit(1)

    logging.info("All tests passed successfully.")

    # Run e2e tests if args is ['e2e']
    result = pytest.main(['tests'])

    if result != 0:
        logging.error("Some tests failed.")
        logging.shutdown()
        exit(1)

    logging.info("All tests passed successfully.")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f"Test suite failed: {e}")
        logging.shutdown()
        exit(1)
