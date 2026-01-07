from src.extract.extract_dates import extract_dates
from src.extract.call_limit import base_api
import pandas as pd


# Test function to validate date extraction
def test_extract_dates():
    dates_df = extract_dates(base_api)
    assert isinstance(dates_df, pd.DataFrame)
    assert not dates_df.empty
