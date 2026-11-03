from dataFileUploader import data_File_Uploader

def main():

    print("================================")
    print("   DATA ANALYTICS PLATFORM")
    print("================================")

    dataset = data_File_Uploader()

    if  dataset is  None:
        print("dataset is loading...")
        return

    print("=====Dataset======")
    print(f"total_rows : {dataset.shape[0]}")
    print(f"total_cols : {dataset.shape[1]}")

    print(f"dataset_columns_name : {dataset.columns.to_list()}")

    df = dataset

    print(df)
    
    # print(f"dataset preview : {dataset.head(4)}")


if __name__ == "__main__":
    main()    