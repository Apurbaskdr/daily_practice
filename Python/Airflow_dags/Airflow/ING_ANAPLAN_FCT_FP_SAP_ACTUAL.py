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


load_raw=SnowflakeOperator(
    task_id="load_raw",
    sql="{{ ti.xcom_pull(key='load_raw_query') }}",
    snowflake_conn_id="snowflake_conn_raw_anaplan",
    dag=dag
)


def get_raw_count_load_table(dag_run=None,**context):
    raw_db=context['ti'].xcom_pull(key='RAW_DB').lower()
    raw_table=context['ti'].xcom_pull(key='RAW_TABLE').lower()
    filename=context['ti'].xcom_pull(key='FILENAME')
    timestamp=context['ti'].xcom_pull(key='FILE_TIME_STAMP')
    trusted_table=context['ti'].xcom_pull(key='TRUSTED_TABLE')
    
    dbt_args=["dbt test -s source:%s.%s" %(raw_db,raw_table), "dbt build --exclude resource_type:test --vars '{\"FILENAME\": \"%s\", \"FILE_TIME_STAMP\": \"%s\"}' -s %s" %(filename,timestamp,trusted_table) ]
    
    exec_status, run_job=call_dbt_job_branch(dbt_args, context, dag)