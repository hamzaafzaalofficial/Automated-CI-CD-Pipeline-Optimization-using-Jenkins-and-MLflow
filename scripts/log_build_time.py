import mlflow
import time
import sys
import os

mlflow.set_tracking_uri(os.environ.get('MLFLOW_TRACKING_URI', 'http://192.168.122.1:5000'))

build_number = sys.argv[1] if len(sys.argv) > 1 else 'unknown'


with mlflow.start_run():
    start_time = time.time()
    time.sleep(60)  # Simulate build time
    build_time = time.time() - start_time
    mlflow.log_metric('build_time', build_time)
    mlflow.set_tag('stage', 'build')
    mlflow.log_param('build_number', build_number)
    