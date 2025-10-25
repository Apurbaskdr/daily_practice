import os
import pandas as pd



def reverse_s(s):
    rs=''
    for i in s:
        rs=i+rs
    return rs


def fileList(location,extention):
    os.chdir(location)
    #file_list=[i for i in os.listdir() if i==file_name and file_name.endswith(extention)]
    file_list=[i for i in os.listdir() if i.endswith(extention)]
    return file_list

def filePresence(file_name,location,extention):
    os.chdir(location)
    file_list=[i for i in os.listdir() if i==file_name and file_name.endswith(extention)]
    return file_list


def convert_to_csv(location,location_to_place,file_name):
    extention='.csv'
    if file_name == '':
        file_list_to_convert=fileList(location,extention)
    else:
        file_list_to_convert=fileList(file_name,location,extention)
    
    for file in file_list_to_convert:
        output_file_name=file.split('.').replace(' ','_') + '.csv'
        output_file_location=location_to_place+'/'+output_file_name
        df=pd.read_excel(file)
        df.to_csv(output_file_location, index=False)


def csv_files_with_lines(file_name,h_line,t_line):
    df=pd.read_csv(file_name)
    subset_dataframe=df.iloc[h_line,t_line]
    return subset_dataframe

def csv_file_details(file_name):
    file_to_know=file_name
    df=pd.read_csv(file_to_know)
    cols=df.columns
    d_type=df.dtypes
    d_shape=df.shape
    print('Columns: ',cols)
    print('DataFrame DataTypes: ',d_type)
    print('DataFrame Shape: ',d_shape)


