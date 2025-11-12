from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator
from airflow.providers.dbt.cloud.hooks.dbt import DbtCloudHook
import boto3
from airflow.models import Variable
import json
from datetime import time






def call_dbt_job_branch(dbt_args, context, dag):
    run_job= dbt_job(dbt_args, context, dag)
    try:
        run_job.execute(context)
        return "success", "run_job not required"
    
    except Exception as e:
        return "failure", run_job
    

def call_dbt_job_branch_with_warn(dbt_args, context, dag):
    run_job= dbt_job(dbt_args, context, dag)
    try:
        run_job.execute(context)
        return "success", run_job
    except Exception as e:
        return 'failure', run_job
    
    
def dq_test_status(run_job, failure_pattern):
    run_id=run_job.run_id
    hook=DbtCloudHook('dbtcloud_conn_anaplan')
    runinfo=hook.get_job_run(run_id, include_related=["run_steps"])
    data=runinfo.json()
    run_steps=data['data']['run_steps']
    run_id= run_steps[0]['run_id']
    for i in run_steps:
        print (i['name'])
        print (i['logs'])
        print (i['status_humanized'])
        print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    
    build_step=next((step for step in run_steps if step['name'].startswith('Invoke bdt with `dbt test --`')))
    
    
def dbt_job(dbt_args, context, dag):
    s3_resource=boto3.resource('s3')
    json_file_path='dbtcloud_jobs/anaplan/dbtcloud_jobs.json'
    bucket_name='adp-' + Variable.get("ADP_ENVIRONMENT").lower() + '-airflow-environment'
    content_object= s3_resource.Object(bucket_name, json_file_path)
    file_content=content_object.get()['Body'].read().decode('utf-8')
    dbtcloudjobs= json.loads(file_content)
    dag_id=context['task_instance'].dag_id
    job_id=dbtcloudjobs[dag_id]
    run_job= DbtCloudRunJobOperator(
        task_id="run_job" + str(time.time_ns()),
        dbt_cloud_conn_id='dbtcloud_conn_anaplan',
        steps_override=dbt_args,
        job_id=job_id,
        wait_for_termination=True,
        timeout=3600,
        dag=dag
    )
    return run_job


