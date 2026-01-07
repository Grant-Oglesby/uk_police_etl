from src.transform.transform import transform
import pandas as pd


# Need to confirm what columns and datatypes are expected
# Will use .ipynb to determine this

# Confirm that dataframe has no null values
def test_transform_nulls(df):
    df = transform(df)
    assert df.isnull().sum().sum() == 0


# Confirm that output is a pandas dataframe
def test_dataframe_type(df):
    df = transform(df)
    assert isinstance(df, pd.DataFrame)


# Confirm that dataframe has expected columns
def test_dataframe_columns(df):
    df = transform(df)
    expected_columns = [
        # Add expected column names here
    ]
    assert all(column in df.columns for column in expected_columns)


# Confirm that dataframe is not empty
def test_dataframe_rows(df):
    df = transform(df)
    assert not df.empty


# Confirm that dataframe has expected datatypes for columns
def test_dataframe_dtypes(df):
    df = transform(df)
    expected_dtypes = {
        # Add expected dtypes here
    }
    for column, dtype in expected_dtypes.items():
        assert df[column].dtype == dtype


# Confirm formatting of specific columns if necessary
def test_column_formatting(df):
    df = transform(df)
    # Add specific formatting checks here
    # Example: Check if date columns are in datetime format
