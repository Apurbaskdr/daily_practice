from datetime import datetime
import logging
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from subprocess import PIPE, Popen
import re


def get_file_list(input_s3_loc):
    logging.info("Getting all the file list")
    process= Popen("aws s3 ls "+input_s3_loc+" | awk '{print $1$2$4}'", shell=True, stdout=PIPE, stderr=PIPE)
    std_out, std_err = process.communicate()
    print (std_out, std_err)
    list_of_file_name=std_out.decode("utf-8").split("\n")[0:]
    return list_of_file_name
    

def file_check(file_prefix, file_extension, input_s3_loc, dag_run=None,**kwargs):
    try:
        logging.info("Start for the file download")
        list_of_file_names=get_file_list(input_s3_loc)
        print ("List of file names: ", list_of_file_names)
        pattern= file_prefix + '(.*?)' + file_extension
        reg_file_filter=re.compile(r'^' + pattern + '$')
        execution_time=dag_run.conf.get('execution_time')
        filtered_file_to_download= list([x for x in list_of_file_names if reg_file_filter.match(str(x)[18:]) and datetime.strptime(str(x)[0:18], '%Y-%m-%d%H:%M:%S') <= datetime.strptime(execution_time,'%Y-%m-%d%H:%M:%S')])
        sorted_list=sorted(filtered_file_to_download, key=lambda x: datetime.strptime((str(x).split(".")[0])[-19:],'%Y-%m-%d%H:%M:%S'), reverse=False)
        return sorted_list
    except Exception as e:
        logging.info("File fetch failed with error: "+str(e))
        return e
        
    


def trigger_ingestion_dag(raw_table,trusted_table,object_name,trigger_workflow,file_check_task,**context):
    try:
        sortedFileList=context['ti'].xcom_pull(task_id='file_check_task')
        for input_file in sortedFileList:
            input_file=input_file[18:]
            input_file_timestamp= datetime.strftime(datetime.strptime((input_file.split(".")[0])[-19],'%Y-%m-%d_%H-%M-%S'), '%Y-%m-%d %H:%M:%S')
            logging.info("Triggering ING flow for: ", input_file)
            trigger_dag=TriggerDagRunOperator(
                task_id="trigger_dag_{}".format(input_file),
                trigger_dag_id=trigger_workflow,
                wait_for_completion=True,
                conf={
                    'FILENAME': input_file, 'FILE_TIME_STAMP': input_file_timestamp, 'RAW_TABLE': raw_table, 'TRUSTED_TABLE':trusted_table, 'OBJECT_NAME': object_name}) 
            trigger_dag.execute(context)
            
    except Exception as e:
        logging.info("File Fetched with error: "+ str(e))
        raise e
            