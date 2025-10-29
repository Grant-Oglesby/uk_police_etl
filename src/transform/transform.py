import pandas as pd


def extrapolate_long_lat(crime_data_df):
    # Extract latitude and longitude from location column
    crime_data_df = crime_data_df.assign(
        latitude=crime_data_df['location'].apply(
            lambda x: eval(x)['latitude'] if pd.notnull(x) else x
        ),
        longitude=crime_data_df['location'].apply(
            lambda x: eval(x)['longitude'] if pd.notnull(x) else x
        )
    )
    return crime_data_df


def merge_forces_crime_df(crime_data_df, forces_df):
    # Merge forces and crime data dataframes on 'force_id' column
    forces_df = forces_df.rename(columns={'id': 'force_id'})
    forces_df['force_id'] = forces_df['force_id'].astype(str)
    crime_data_df['force_id'] = crime_data_df['force_id'].astype(str)
    crime_data_df = crime_data_df.merge(forces_df, on='force_id', how='left')
    return crime_data_df


def extract_date_time(crime_data_df):
    # Extract date and time components from 'date' column
    crime_data_df['date'] = pd.to_datetime(
        crime_data_df['datetime']
    ).dt.strftime('%d-%m-%Y')
    crime_data_df['time'] = pd.to_datetime(
        crime_data_df['datetime']
    ).dt.strftime('%H:%M:%S')
    return crime_data_df


def drop_unnecessary_columns(crime_data_df):
    # Identify columns to drop
    columns_to_drop = [
        'outcome_object',                       # Outcome already recorded
        'location',                             # Lat and Long extracted
        'force_id',                             # Replaced by 'force_name'
        'operation',                            # Unused column
        'operation_name',                       # Unused column
        'removal_of_more_than_outer_clothing',  # Not needed for analysis
        'datetime',                             # Date and Time extracted
        'outcome_linked_to_object_of_search'    # 49% missing values
    ]

    # Drop specified columns
    crime_data_df = crime_data_df.drop(columns=columns_to_drop)
    return crime_data_df


def fill_na(crime_data_df):
    # Fill null values with Not Recorded to infer missing data correlations
    crime_data_df = crime_data_df.fillna('Not Recorded')
    return crime_data_df


def define_dtypes(crime_data_df):
    # Define appropriate data types for each column
    crime_data_df = crime_data_df.astype(
        {
            'age_range': 'category',
            'outcome': 'category',
            'involved_person': 'bool',
            'self_defined_ethnicity': 'category',
            'gender': 'category',
            'legislation': 'category',
            'officer_defined_ethnicity': 'category',
            'type': 'category',
            'object_of_search': 'category',
            'latitude': 'object',
            'longitude': 'object',
            'name': 'category',
            'date': 'datetime64[ns]',
            'time': 'datetime64[ns]'
        }
    )
    return crime_data_df


def main(raw_df_list):
    forces_df = raw_df_list[0]
    crime_data_df = raw_df_list[2]
    crime_data_df = extrapolate_long_lat(crime_data_df)
    crime_data_df = merge_forces_crime_df(crime_data_df, forces_df)
    crime_data_df = extract_date_time(crime_data_df)
    crime_data_df = drop_unnecessary_columns(crime_data_df)
    crime_data_df = fill_na(crime_data_df)
    crime_data_df = define_dtypes(crime_data_df)
    return crime_data_df
