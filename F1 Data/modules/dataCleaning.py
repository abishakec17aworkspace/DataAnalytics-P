
import pandas as pd


def dataCleaning(df: pd.DataFrame):

    cleaned_df = df.copy()

    print("\n========== DATA CLEANING MODULE ==========")

    # STEP 1: Standardize Column Names

    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("\nStandardized Column Names:")
    print(list(cleaned_df.columns))


    # STEP 2: Missing Value Assessment

    print("\n========== MISSING VALUE ASSESSMENT ==========")

    print("\nMissing Values Before Cleaning:")
    print(cleaned_df.isnull().sum())

    print("\nTotal Missing Values:")
    print(cleaned_df.isnull().sum().sum())


    # STEP 3: Fill Categorical Missing Values

    categorical_columns = [
        "driver",
        "team",
        "weather",
        "tyre_compound"
    ]

    for column in categorical_columns:

        if column in cleaned_df.columns:

            cleaned_df[column] = cleaned_df[column].fillna("Unknown")


    # STEP 4: Fill Numerical Missing Values

    numerical_fill_columns = ["overtakes"]

    for column in numerical_fill_columns:

        if column in cleaned_df.columns:

            median_value = cleaned_df[column].median()

            cleaned_df[column] = cleaned_df[column].fillna(
                median_value
            )


    # STEP 5: Preserve Meaningful Missing Values

    # finish_position missing values may represent
    # DNF, DNS, or DSQ. Therefore, preserve them.

    if "finish_position" in cleaned_df.columns:

        print("\nMissing finish_position values preserved:",
              cleaned_df["finish_position"].isnull().sum())


    # STEP 6: Duplicate Record Assessment

    print("\n========== DUPLICATE RECORD ASSESSMENT ==========")

    duplicate_count = cleaned_df.duplicated().sum()

    print("\nDuplicate Records Before Removal:")
    print(duplicate_count)

    cleaned_df = cleaned_df.drop_duplicates()

    print("\nDuplicate Records After Removal:")
    print(cleaned_df.duplicated().sum())


    # STEP 7: Data Type Assessment

    print("\n========== DATA TYPE ASSESSMENT ==========")

    print("\nData Types Before Conversion:")
    print(cleaned_df.dtypes)


    # STEP 8: Data Type Correction

    numerical_columns = [
        "season",
        "round",
        "grid_position",
        "qualifying_position",
        "finish_position",
        "points_scored",
        "pit_stops",
        "fastest_lap_seconds",
        "race_duration_minutes",
        "overtakes"
    ]

    for column in numerical_columns:

        if column in cleaned_df.columns:

            cleaned_df[column] = pd.to_numeric(
                cleaned_df[column],
                errors="coerce"
            )


    # STEP 9: Final Data Quality Verification

    print("\n========== FINAL CLEANING REPORT ==========")

    print("\nMissing Values After Cleaning:")
    print(cleaned_df.isnull().sum())

    print("\nTotal Missing Values After Cleaning:")
    print(cleaned_df.isnull().sum().sum())

    print("\nFinal Data Types:")
    print(cleaned_df.dtypes)

    print("\nFinal Dataset Shape:")
    print(cleaned_df.shape)


    # STEP 10: Return Cleaned Dataset

    return cleaned_df
