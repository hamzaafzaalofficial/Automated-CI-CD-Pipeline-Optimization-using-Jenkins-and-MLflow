import mlflow
import time
import sys
import os


build_number = sys.argv[1] if len(sys.argv) > 1 else 'unknown'

mlflow.set_tracking_uri(os.environ.get('MLFLOW_TRACKING_URI', 'http://localhost:5000'))

with mlflow.start_run():
    start_time = time.time()
    time.sleep(300)  # Simulate deploy time
    deploy_time = time.time() - start_time
    mlflow.log_metric('deploy_time', deploy_time)
    mlflow.set_tag('stage', 'deploy')
    mlflow.log_param('build_number', build_number)