from modules.dataFileUploader import data_File_Uploader
from modules.dataQualityAssesment import dataQualityAssesment
from modules.dataInspection import dataInspection
from modules.dataCleaning import dataCleaning

def main():

    df = data_File_Uploader()

    if df is None:
        print("Dataset collection failed...")
        return 

    print("The Dataset Collectd is.....")
    # print(df.head().to_string(index=False))

    check = input("Want to check Data Inspection : ")
    if check == '1':
        print("====== QA ======")
        dataInspection(df)
          
    check = input("Want to check Quality Assesment : ")
    if check == '2':
        print("====== QA ======")
        dataQualityAssesment(df)

    check = input("Want to check Cleaned Dataset Column : ")
    if check == '3':
        print("====== QA ======")
        dataCleaning(df)  
    

if __name__ == "__main__":
     main()