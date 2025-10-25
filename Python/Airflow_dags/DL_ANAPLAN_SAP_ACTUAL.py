from datetime import datetime
from airflow import DAG
import logging
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.python_operator import PythonOperator
from lib.myLib import *
from lib.daglib import *
from lib.audit_table import *
from namespace.a_namespace import *


logging.basicConfig(level=logging.INFO)
logger = logging(__name__)

file_prefix="Anaplan_sap_actual_2"
file_extension='.csv'
raw_table='raw_fct_fp_sap_actual'
raw_db='raw_anaplan'
trusted_table='trusted_fct_fp_sap_actual'
refined_table='fct_fp_sap_actual'
object_name='fct_fp_sap_actual'
trigger_workflow='ING_ANAPLAN_FCT_FP_SAP_ACTUAL'

args={
    'owner':'airflow',
    'start_date':datetime(2022,01,01),
    'on_failure_callback':audit_logs
}


with DAG(
    dag_id='DL_ANAPLAN_SAP_ACTUAL',
    catch_up=False,
    on_success_callback=cal_audit_logs,
    default_args=args,
    schedule_interval=None,
    tag=["Anaplan"]
) as dag:
    s3_to_adp_load=PythonOperator(
        task_id="s3_to_adp_load",
        python_callable=s3_to_adp_load_ignore_execution_time,
        provide_context=True,
        dag=dag,
        do_xcom_push=True,
        op_kwargs={'file_prefix':file_prefix, 'file_extension':file_extension, 'input_s3_loc':A_NAMESPACE['INPUT_S3_LOCATION']}
    )
    
    trigger_ingestion_dag=PythonOperator(
        task_id=trigger_ingestion_dag,
        python_callable=trigger_ingestion_dag,
        provide_context=True,
        dag=dag,
        do_xcom_push=True,
        op_kwargs={'raw_table':raw_table, 'trusted_table': trusted_table, 'object_name': object_name, 'trigger_workflow': trigger_workflow, 's3_to_adp_load_task': 's3_to_adp_load'}
    )