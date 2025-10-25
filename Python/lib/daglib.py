import logging
from subprocess import PIPE, Popen
import re
from datetime import datetime

def s3_to_adp_load_ignore_execution_time(file_prefix, file_extension, input_s3_loc, **kwargs):
    try:
        logging.info("Start for the file download...")
        process=Popen("aws s3 ls " + input_s3_loc + " | '{print $1$2$4}'", shell=True, stdout=PIPE, strerr=PIPE)
        std_out, std_err=process.communicate()
        print(std_out, std_err)
        list_of_file_name= std_out.decode("utf-8").split('\n')[0:]
        pattern=file_prefix + '(.*?)' + file_extension
        reg_file_filter=re.compile(r'^' + pattern + '$')
        execution_time="2030-01-0101:01:01"
        print ("Execution_Time: "+ execution_time)
        filtered_list_to_download=list([x for x in list_of_file_name if reg_file_filter.match(str(x)[18:]) and datetime.strptime(str(x)[0:18], '%Y-%m-%d%H:%M:%S') <= datetime.strptime(execution_time, '%Y-%m-%d%H:%M:%S')])
        sortedFileList=sorted(
            filtered_list_to_download,
            key=lambda x: datetime.strptime((str(x).split(".")[0])[-19:], '%Y-%m-%d%H:%M:%S'),
            reverse=False
        )
        print(sortedFileList)
        logging.info("File Fetch Completed")
        return sortedFileList
    except Exception as e:
        logging.info("File fetch failed with error" + e)
        raise e


def s3_to_adp_load(file_prefix, file_extension, input_s3_loc, dag_run=None, **kwargs):
    try:
        logging.info("Start for the file download...")
        process=Popen("aws s3 ls " + input_s3_loc + " | awk '{print $1$2$4}'", shell=True, stdout=PIPE, stderr=PIPE)
        std_out, std_err= process.communicate()
        print(std_out, std_err)
        list_of_file_names=std_out.decode("utf-8").split('\n')[0:]
        print(list_of_file_names)
        pattern=file_prefix + '(.*?)' + file_extension
        reg_file_filter=re.compile(r'^' + pattern + '$')
        now=datetime.now()
        execution_time=dag_run.conf.get('execution_time')
        print(execution_time)
        filtered_file_name_to_download=list([x for x in list_of_file_names if reg_file_filter.match(str(x)[18:]) and datetime.strptime(str(x)[0:18], '%Y-%m-%d%H:%M:%S') <= datetime.strptime(execution_time,  '%Y-%m-%d%H:%M:%S')])
        sortedFileList=sorted(
            filtered_file_name_to_download,
            key=lambda x: datetime.strptime((str(x).split(".")[0])[-19:], '%Y-%m-%d%H:%M:%S'),
            reverse=False
        )
        print(sortedFileList)
        print(filtered_file_name_to_download)
        logging.info("File Fetch Completed")
        return sortedFileList
    except Exception as e:
        logging.info("File Fetch Failed with Error" + e)
        raise e