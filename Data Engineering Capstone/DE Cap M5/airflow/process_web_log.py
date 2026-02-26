from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# -----------------------------
# DAG Default Arguments
# -----------------------------
default_args = {
    'owner': 'Mohammad',                     # Your name or team
    'start_date': datetime(2024, 1, 1),      # Any past date
    'email': ['your_email@example.com'],     # Any valid email
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# -----------------------------
# Define the DAG
# -----------------------------
dag = DAG(
    dag_id='process_web_log',
    default_args=default_args,
    description='Daily pipeline to extract, filter, and archive web server log data',
    schedule_interval='@daily',
    catchup=False
)

# -----------------------------
# Create a task to extract data
# -----------------------------
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -d " " -f 1 /home/project/airflow/dags/capstone/accesslog.txt > /home/project/airflow/dags/capstone/extracted_data.txt',
    dag=dag
)

# -----------------------------
# Create a task to transform data
# -----------------------------
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v "198.46.149.143" /home/project/airflow/dags/capstone/extracted_data.txt > /home/project/airflow/dags/capstone/transformed_data.txt',
    dag=dag
)

# -----------------------------
# Create a task to Load data
# -----------------------------
load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -cvf /home/project/airflow/dags/capstone/weblog.tar -C /home/project/airflow/dags/capstone transformed_data.txt',
    dag=dag
)

# -----------------------------
# Define task pipeline
# -----------------------------
extract_data >> transform_data >> load_data
