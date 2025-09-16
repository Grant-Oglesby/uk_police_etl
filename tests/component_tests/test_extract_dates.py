from src.extract.extract_dates import extract_dates
import pandas as pd

test_file = 'tests/test_data/sample_crime_data.json'


# Test function to validate date extraction
def test_extract_dates(test_file):
    dates_df = extract_dates(test_file)
    assert isinstance(dates_df, pd.DataFrame)
    assert not dates_df.empty


if __name__ == "__main__":
    test_extract_dates(test_file)
    print("All tests passed.")
