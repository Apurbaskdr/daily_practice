from airflow import DAG
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.python_operator import PythonOperator
from lib.myLib import *


file_prefix='new_file_2'
file_extension='.csv'
raw_db='raw_customer'
raw_table='raw_table_name'
trusted_db='customer'
trusted_table='trusted_new_table'
s3_path='s3://'
trigger_workflow='CHILD_DAG_TO_PROCESS'



args={
    'owner':'Apurba',
    'start_date':datetime(2022,09,22)
}


with DAG(
    dag_id='PARENT_DAG_TO_PROCESS',
    catchup=False,
    default_args=args,
    schedule_interval=None,
    tags=["Apurba"]
) as dag:
    file_check= PythonOperator(
        task_id="file_check",
        provide_context=True,
        dag=dag,
        do_xcom_push=True,
        ok_kwargs={'file_prefix':file_prefix, 'file_extension':file_prefix, 'input_s3_loc':s3_path}
    )
    
    trigger_ingestion_dag=PythonOperator(
        task_id="trigger_ingestion_dag",
        python_callable=trigger_ingestion_dag,
        provide_context=True,
        dag=dag,
        do_xcom_push=True,
        op_kwargs={
            'raw_db':raw_db, 'raw_table':raw_table, 'trusted_db': trusted_db, 'trusted_table':trusted_table
        }
    )