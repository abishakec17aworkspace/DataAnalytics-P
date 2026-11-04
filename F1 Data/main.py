from modules.dataFileUploader import data_File_Uploader
from modules.dataQualityAssesment import dataQualityAssesment
from modules.dataInspection import dataInspection

def main():

    df = data_File_Uploader()

    if df is None:
        print("dataset collection failed...")
        return 

    print(" the Dataset Collectd is.....")
    # print(df.head().to_string(index=False))

    check = input("want to check Data Inspection : ")
    if check == "yes":
        print("====== QA ======")
        dataInspection(df)
        
    
    check = input("want to check Quality Assesment :")
    if check == "yes":
        print("====== QA ======")
        dataQualityAssesment(df)
    

if __name__ == "__main__":
     main()
