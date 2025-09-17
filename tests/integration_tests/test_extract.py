from src.extract.extract import extract
import pandas as pd


# Test data received from the extract function
# Expected output is a list of two dataframes, one for forces and one for
# crime data
def test_extract():
    test_Data = extract()
    assert isinstance(test_Data, list)
    assert len(test_Data) > 0
    assert isinstance(test_Data[0], pd.DataFrame)
    assert isinstance(test_Data[1], pd.DataFrame)
    assert isinstance(test_Data[2], pd.DataFrame)
    assert len(test_Data[0]) > 0
    assert len(test_Data[1]) > 0
    assert len(test_Data[2]) > 0
