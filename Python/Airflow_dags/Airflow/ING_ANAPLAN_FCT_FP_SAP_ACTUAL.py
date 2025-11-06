from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
import logging




logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
args={
    'owner':'airflow',
    'start_date': datetime(2022,1,1),
    'on_failure_callback':audit_logs
}

dag=DAG(
    dag_id="ING_ANAPLAN_FCT_FP_SAP_ACTUAL",
    catchup=False,
    schedule_interval=None,
    on_success_callback=audit_logs,
    default_args=args,
    tags=['Anaplan']
)

'''catchup=False, Do NOT run past scheduled tasks. Only run from the time the DAG is turned on / deployed or the current execution date onward'''


raw_truncate=SnowflakeOperator(
    task_id="raw_truncate",
    sql="{{ ti.xcom_pull(key='truncate_query') }}",
    snowflake_connection_id="snowflake_conn_raw_anaplan",
    dag=dag
)
