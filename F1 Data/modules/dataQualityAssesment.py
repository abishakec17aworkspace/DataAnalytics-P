
import pandas as pd


def dataQualityAssesment(df: pd.DataFrame):

    print("======== Data Quality Assessment Report ========")

    # 1. Missing values by column
    print("\nMissing Values By Column:")
    print(df.isnull().sum())

    # 2. Total missing values
    print("\nTotal Missing Values:")
    print(df.isnull().sum().sum())

    # 3. Missing percentage
    print("\nMissing Percentage:")
    missing_percentage = (df.isnull().sum() / len(df)) * 100
    print(missing_percentage.round(2))

    # 4. Rows containing missing values
    print("\nRows Containing Missing Values:")
    missing_rows = df[df.isnull().any(axis=1)]
    print(missing_rows)

    print("\nTotal Rows Containing Missing Values:")
    print(len(missing_rows))

    # 5. Duplicate records
    print("\nDuplicate Records Count:")
    print(df.duplicated().sum())

    # 6. Display duplicated data
    print("\nDuplicated Data:")
    print(df[df.duplicated()])

    # 7. Column data types
    print("\nColumn Data Types:")
    print(df.dtypes)
