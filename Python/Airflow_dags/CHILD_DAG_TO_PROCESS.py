import logging
from datetime import datetime
from airflow import DAG
from airflow.contrib.hooks.snowflake_hook import SnowflakeOperator



logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
args= {
    'owner': 'Apurba',
    'start_date': datetime(2022,1,1)
}


dag=DAG(
    dag_id="CHILD_DAG_TO_PROCESS",
    catchup=False,
    schedule_time=None,
    default_args=args,
    tags=["Apurba"]
)


raw_truncate= SnowflakeOperator(
    task_id="raw_truncate"
    sql="select * from customer"
    snowflake_conn_id="snow_con"
    dag=dag
)