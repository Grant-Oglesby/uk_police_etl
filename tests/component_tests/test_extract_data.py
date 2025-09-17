from src.extract.extract_data import extract_data
from src.extract.call_limit import base_api
import pandas as pd


# Test data received from extract_data function
# Will use a modified API call that includes data from forces dataframe
# Expected output is crime data in dataframe format
def test_extract_data():
    # Setup local file path for test data
    test_forces_df = pd.read_csv('data/test/test_force.csv')
    test_dates_df = pd.read_csv('data/test/test_date.csv')
    test_Data = extract_data(base_api, test_forces_df, test_dates_df)
    assert isinstance(test_Data, pd.DataFrame)
    assert len(test_Data) > 0
