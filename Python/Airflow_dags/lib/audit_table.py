from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
import logging
from airflow.models import Variable
from airflow.kubernetes.secret import Secret

kube_config_path='/usr/local/airflow/dags/kube_config.yml'


def cal_audit_logs(db, name, task,arguments, context):
    try:
        logging.info("Triggering Kubernetes DBT: "+ name)
        print(arguments)
        call_kubop=KubernetesPodOperator(
            namespace="mwaa",
            image="401003852533.dkr.ecr.us-east-1.amazonaws.com/" + Variable.get("A_ENVIRONMENT").lower() + "alxn-data-comm-" + db.lower() + ":latest",
            arguments=arguments,
            name=name,
            labels={"task": name},
            get_logs=True,
            is_delete_operator_pod=False,
            config_file=kube_config_path,
            is_cluster=False,
            cluster_context='aws',
            env_vars={
                "SNOWFLAKE_ACCOUNT": Variable.get("SNOWFLAKE_ACCOUNT"),
                "SNOWFLAKE_DB": Variable.get("SNOWFLAKE_DB"),
                "SNOWFLAKE_ROLE": Variable.get("SNOWFLAKE_ROLE"),
                "SNOWFLAKE_SCHEMA": Variable.get("SNOWFLAKE_SCHEMA"),
                "SNOWFLAKE_WAREHOUSE": Variable.get("SNOWFLAKE_WAREHOUSE"),
                "SNOWFLAKE_USER": Variable.get("SNOWFLAKE_USER"),
                "SNOWFLAKE_PASSWORD": Variable.get("SNOWFLAKE_PASSWORD")
            }
        ) 
        call_kubop.execute(context)
    except Exception as e:
        logging.info("Kubernetes operator falied with error: " + str(e))
        raise e