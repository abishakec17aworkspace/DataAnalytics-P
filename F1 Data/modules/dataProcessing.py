
import pandas as pd


def dataProcessing(df: pd.DataFrame):

    processed_df = df.copy()

    print("\n========== DATA PROCESSING MODULE ==========")


    # STEP 1: Filtering

    print("\n========== FILTERING ==========")

    season_2024 = processed_df[
        processed_df["season"] == 2024
    ]

    print("\nRecords for 2024 Season:")
    print(season_2024.head())


    # STEP 2: Sorting

    print("\n========== SORTING ==========")

    sorted_data = processed_df.sort_values(
        by="points_scored",
        ascending=False
    )

    print("\nTop 10 Records by Points:")
    print(sorted_data.head(10))


    # STEP 3: Grouping

    print("\n========== GROUPING ==========")

    driver_summary = processed_df.groupby("driver").agg(
        total_points=("points_scored", "sum"),
        average_points=("points_scored", "mean"),
        total_records=("round", "count")
    )

    print("\nDriver Performance Summary:")
    print(driver_summary)


    # STEP 4: Create Derived Columns

    print("\n========== DERIVED COLUMNS ==========")

    processed_df["grid_qualifying_difference"] = (
        processed_df["qualifying_position"] -
        processed_df["grid_position"]
    )

    print("\nNew Column Created:")
    print("grid_qualifying_difference")


    # STEP 5: Return Processed Dataset

    return processed_df
