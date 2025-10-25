import os
import pandas as pd

file_path='D:/Practice/daily_practice/Python/file_path'
os.chdir(file_path)
curr_path=os.getcwd()
dir_list=os.listdir()
print (dir_list)
extention='.csv'
files_to_convert=[]
'''for file in dir_list:
    if file.endswith('.xlsx'):
        files_to_convert.append(file)
print (files_to_convert)'''

files_to_convert=[i for i in os.listdir() if i.endswith(extention)]
print (files_to_convert)

for file in files_to_convert:
    print("File_name: ", file)
    df=pd.read_csv(file)
    cols=df.columns
    d_type=df.dtypes
    d_shape=df.shape
    print('Columns: ',cols)
    print('DataFrame DataTypes: ',df.dtypes)
    print('DataFrame Shape: ',d_shape)

'''for c_file in files_to_convert:
    output_file_name=c_file.split('.')[0].replace(' ','_') +'.csv'
    print (output_file_name)
    df=pd.read_excel(c_file)
    df.to_csv(output_file_name, index=False)'''