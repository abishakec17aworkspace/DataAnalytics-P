import pandas as pd

def data_File_Uploader():

    print("============= CSV Analyzer =============")
    file_path = input("Enter the CSV filePath: ")

    try:
        df = pd.read_csv(file_path)
        print("\n CSV uploaded sucessfully...")

        return df
    
    except FileNotFoundError:
        print("File not found")

    except pd.errors.EmptyDataError:

        print("Error: The CSV file is empty.")

    except Exception as error:

        print(f"Unexpected error: {error}")

    return None        
