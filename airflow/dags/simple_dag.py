from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    'HauVT12_DAG_01',
    default_args = {
        'email' : 'thanhhau217@gmail.com',
        'email_on_failure' : True,
        'retries' : 1,
        'retry_delay' : timedelta(minutes=5)
    },
    description = 'A simple DAG sample by HauVT12',
    schedule_interval = "@once",
    start_date = datetime(2024,4,21),
    tags=['HauVT12'],
)

t1 = BashOperator(
    task_id = 'print_date',
    bash_command = 'date > /tmp/date.txt',
    dag = dag
)

t2 = BashOperator(
    task_id = 'sleep',
    bash_command = 'sleep 5',
    retries = 3,
    dag = dag
)

t3 = BashOperator(
    task_id = 'echo',
    bash_command = 'echo task 3 running',
    dag = dag
)

t1 >> t2 >> t3
 