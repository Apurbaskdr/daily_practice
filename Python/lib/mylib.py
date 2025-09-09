import os

class lib:
    def reverse_s(s):
        rs=''
        for i in s:
            rs=i+rs
        return rs
    
    
    def csv2text(file_name,location):
        os.chdir(location)
        file_list=[i for i in os.listdir() if i==file_name and file_name.endswith('.csv')]
        return file_list