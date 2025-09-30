from datetime import datetime
import logging
from airflow.operators.trigger_dagrun import TriggerDagRunOperator



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
            