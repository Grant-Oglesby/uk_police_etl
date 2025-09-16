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


if __name__ == "__main__":
    test_extract()
    print("All tests passed.")
