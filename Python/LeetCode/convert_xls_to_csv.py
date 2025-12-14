import pandas as pd
import os


file_path='D:/Practice/Files'


def xlsx_to_csv(file_path):
    list_file=os.listdir(file_path)
    print(list_file)
    files_to_convert=[]
    for file in list_file:
        if file.endswith('.xlsx'):
            converted_file=file_path+'/'+file.split('.')[0]+'.csv'
            files_to_convert=file_path+'/'+file
            print(files_to_convert)
            df=pd.read_excel(files_to_convert)
            df.to_csv(converted_file,index=False)
            columns=df.columns()
            print(columns)
            