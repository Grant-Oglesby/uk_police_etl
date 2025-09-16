from src.extract.extract_forces import extract_forces
import pandas as pd

test_file = 'tests/test_data/sample_crime_data.json'


# Test data received from the extract_forces function
# Expected output is a list of police forces in dataframe format
def test_extract_forces(test_file):
    test_Data = extract_forces(test_file)
    assert isinstance(test_Data, pd.DataFrame)
    assert len(test_Data) > 0


if __name__ == "__main__":
    test_extract_forces(test_file)
    print("All tests passed.")
