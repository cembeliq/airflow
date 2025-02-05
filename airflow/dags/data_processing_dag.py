from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def process_data(**context):
    """
    Example data processing function
    """
    try:
        # Add your data processing logic here
        print("Processing data...")
        current_time = datetime.now().isoformat()
        print(f"Generated timestamp: {current_time}")
        result = {
            "processed": True,
            "timestamp": current_time
        }
        print(f"Returning data: {result}")
        return result
    except Exception as e:
        print(f"Error in process_data: {e}")
        return {"processed": False, "timestamp": None}

with DAG(
    'data_processing_pipeline',
    default_args=default_args,
    description='A sample data processing pipeline',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 2, 1),
    catchup=False,
    tags=['provenant'],
) as dag:

    # Create tables if they don't exist
    create_tables = PostgresOperator(
        task_id='create_tables',
        postgres_conn_id='postgres_default',
        sql="""
            CREATE TABLE IF NOT EXISTS processed_data (
                id SERIAL PRIMARY KEY,
                processed_at TIMESTAMP,
                status TEXT
            );
        """
    )

    # Process data
    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
    )

    # Call NestJS API
    api_call = SimpleHttpOperator(
        task_id='call_api',
        http_conn_id='nestjs_api',
        endpoint='/api/data',
        method='POST',
        data="{{ (task_instance.xcom_pull(task_ids='process_data') or {'processed': False, 'timestamp': None}) | tojson }}",
        headers={"Content-Type": "application/json"},
    )

    # Define task dependencies
    create_tables >> process_data_task >> api_call
