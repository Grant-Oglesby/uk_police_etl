from src.extract.extract_data import extract_data
import pandas as pd

# Setup local file path for test data
test_file = 'data/extract/'


# Test data received from extract_data function
# Will use a modified API call that includes data from forces dataframe
# Expected output is crime data in dataframe format
def test_extract_data(test_file):
    test_Data = extract_data(test_file)
    assert isinstance(test_Data, pd.DataFrame)
    assert len(test_Data) > 0


if __name__ == "__main__":
    test_extract_data(test_file)
    print("All tests passed.")
