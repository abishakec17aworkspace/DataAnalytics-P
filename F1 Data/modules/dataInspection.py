import pandas as pd

def dataInspection(df:pd.DataFrame):

     # MODULE 2: DATA UNDERSTANDING
        
        print("\n========== DATASET INSPECTION ==========")
        
        # 1. Dataset dimensions
        print("\nDataset Shape:")
        print(df.shape)
        
        # 2. First 5 records
        print("\nFirst 5 Records:")
        print(df.head())
        
        # 3. Last 5 records
        print("\nLast 5 Records:")
        print(df.tail())
        
        # 4. Column names
        print("\nColumn Names:")
        print(list(df.columns))
        
        # 5. Data types
        print("\nColumn Data Types:")
        print(df.dtypes)
        
        # 6. Dataset technical information
        print("\nDataset Information:")
        df.info()
        
        # 7. Statistical summary
        print("\nStatistical Summary:")
        print(df.describe())
    