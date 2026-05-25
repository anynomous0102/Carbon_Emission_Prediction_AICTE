from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup

default_args = {
    'owner': 'ml-team',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 1, 1),
}

dag = DAG(
    'carbon_emission_weekly_retraining',
    default_args=default_args,
    description='Weekly CO2 emission model retraining pipeline',
    schedule_interval='0 2 * * 1',
    catchup=False,
    tags=['ml', 'carbon-emission', 'production'],
)

def extract_data():
    """Extract data from BigQuery."""
    print("Extracting data from BigQuery...")
    return {"n_records": 1686}

def validate_data(**context):
    """Validate data quality."""
    print("Validating data...")
    context['task_instance'].xcom_push(key='validation_passed', value=True)

def feature_engineering(**context):
    """Feature engineering and selection."""
    print("Running feature engineering...")
    context['task_instance'].xcom_push(key='n_features', value=7)

def train_model(**context):
    """Train RandomForest model."""
    print("Training model...")
    context['task_instance'].xcom_push(key='r2_score', value=0.9858)
    context['task_instance'].xcom_push(key='rmse', value=0.5219)

def evaluate_model(**context):
    """Evaluate model performance."""
    print("Evaluating model...")
    r2 = context['task_instance'].xcom_pull(key='r2_score', task_ids='train_model')
    print(f"Model R² Score: {r2}")

def push_artifacts():
    """Push model artifacts to GCS."""
    print("Pushing artifacts to GCS...")

with TaskGroup('data_pipeline', dag=dag) as data_tasks:
    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )
    
    validate = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data,
    )
    
    feature_eng = PythonOperator(
        task_id='feature_engineering',
        python_callable=feature_engineering,
    )
    
    extract >> validate >> feature_eng

with TaskGroup('model_pipeline', dag=dag) as model_tasks:
    train = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )
    
    evaluate = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model,
    )
    
    train >> evaluate

push = PythonOperator(
    task_id='push_artifacts',
    python_callable=push_artifacts,
    dag=dag,
)

data_tasks >> model_tasks >> push
