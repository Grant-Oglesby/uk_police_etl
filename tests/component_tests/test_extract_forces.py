from src.extract.extract_forces import extract_forces
from src.extract.call_limit import base_api
import pandas as pd


# Test data received from the extract_forces function
# Expected output is a list of police forces in dataframe format
def test_extract_forces():
    test_Data = extract_forces(base_api)
    assert isinstance(test_Data, pd.DataFrame)
    assert len(test_Data) > 0
