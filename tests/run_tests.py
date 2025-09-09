import unittest
import logging

logging.basicConfig(filename='logs/test.log', level=logging.INFO)


def main():
    # Discover and run all tests in the 'tests' directory
    logging.info("Starting test suite...")
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir='tests', pattern='test_*.py')

    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)

    if not result.wasSuccessful():
        logging.error("Some tests failed.")
        logging.shutdown()
        exit(1)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f"Test suite failed: {e}")
        logging.shutdown()
        exit(1)
