
import pandas as pd


def dataExploration(df: pd.DataFrame):

    print("\n========== EXPLORATORY DATA ANALYSIS ==========")

    explored_df = df.copy()


    # STEP 1: Overall Dataset Statistics

    print("\n========== OVERALL STATISTICS ==========")

    print("\nTotal Race Records:")
    print(len(explored_df))

    print("\nTotal Drivers:")
    print(explored_df["driver"].nunique())

    print("\nTotal Teams:")
    print(explored_df["team"].nunique())

    print("\nTotal Seasons:")
    print(explored_df["season"].nunique())

    print("\nTotal Grand Prix:")
    print(explored_df["grand_prix"].nunique())


    # STEP 2: Driver Performance

    print("\n========== DRIVER PERFORMANCE ==========")

    driver_performance = explored_df.groupby("driver").agg(
        total_points=("points_scored", "sum"),
        average_points=("points_scored", "mean"),
        average_finish=("finish_position", "mean"),
        race_records=("record_id", "count")
    )

    driver_performance = driver_performance.sort_values(
        by="total_points",
        ascending=False
    )

    print("\nTop 10 Drivers:")
    print(driver_performance.head(10))


    # STEP 3: Team Performance

    print("\n========== TEAM PERFORMANCE ==========")

    team_performance = explored_df.groupby("team").agg(
        total_points=("points_scored", "sum"),
        average_points=("points_scored", "mean"),
        race_records=("record_id", "count")
    )

    team_performance = team_performance.sort_values(
        by="total_points",
        ascending=False
    )

    print("\nTop Teams:")
    print(team_performance.head(10))


    # STEP 4: Race Status Analysis

    print("\n========== RACE STATUS ANALYSIS ==========")

    race_status_summary = explored_df["race_status"].value_counts()

    print("\nRace Status Distribution:")
    print(race_status_summary)


    # STEP 5: Circuit Analysis

    print("\n========== CIRCUIT ANALYSIS ==========")

    circuit_summary = explored_df.groupby("circuit_name").agg(
        total_records=("record_id", "count"),
        average_points=("points_scored", "mean")
    )

    print("\nCircuit Summary:")
    print(circuit_summary.sort_values(
        by="total_records",
        ascending=False
    ).head(10))


    # STEP 6: Starting Position vs Finishing Position

    print("\n========== POSITION ANALYSIS ==========")

    position_data = explored_df[
        ["grid_position", "finish_position"]
    ].dropna()

    print("\nCorrelation Between Grid and Finish Position:")

    print(
        position_data["grid_position"].corr(
            position_data["finish_position"]
        )
    )


    # STEP 7: Return Explored Dataset

    return explored_df
