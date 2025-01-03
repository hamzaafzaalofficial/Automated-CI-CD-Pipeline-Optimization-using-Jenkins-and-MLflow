pipeline {
    agent any
    environment {
        MLFLOW_TRACKING_URI = 'http://192.168.122.1:5000'
    }
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/hamzaafzaalofficial/Automated-CI-CD-Pipeline-Optimization-using-Jenkins-and-MLflow.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
                sh 'pip install mlflow'
                sh "python3 scripts/log_build_time.py ${BUILD_NUMBER}"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Add your test commands here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh "python3 scripts/log_deploy_time.py ${BUILD_NUMBER}"
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}