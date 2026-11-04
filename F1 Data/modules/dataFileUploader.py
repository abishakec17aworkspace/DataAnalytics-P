
import pandas as pd
from pathlib import Path


def data_File_Uploader():

    print("======= CSV Data Analyzer =======")

    file_path = input("Enter the File_Path: ").strip()

    file_path = Path(file_path)

    # Step 1: Check whether file exists
    if not file_path.is_file():
        print("Error: CSV file not found.")
        return None

    # Step 2: Check file extension
    if file_path.suffix.lower() != ".csv":
        print("Only CSV files are accepted.")
        return None

    # Step 3: Read the CSV file
    try:
        df = pd.read_csv(file_path)

        print("Dataset collected successfully.")

        # IMPORTANT: Return the DataFrame
        return df

    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")

    except pd.errors.ParserError:
        print("Error: Unable to parse the CSV file.")

    except (OSError, UnicodeDecodeError) as error:
        print(f"File reading error: {error}")

    return None
