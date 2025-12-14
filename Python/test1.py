import pandas as pd
import os


file_path='D:/Practice/Files'


list_file=os.listdir(file_path)
print(list_file)
files_to_convert=[]
for file in list_file:
    if file.endswith('.xlsx'):
        files_to_convert=file_path+'/'+file
        print(files_to_convert)
        df=pd.read_excel(files_to_convert)
        columns=df.columns
        print(columns)
        print(df['CUSTOMER_ID']>10)
        df.fillna('NA')
        df.isnull().fillna('NA')
        df.dropna
        print (df)
        df.drop_duplicates()