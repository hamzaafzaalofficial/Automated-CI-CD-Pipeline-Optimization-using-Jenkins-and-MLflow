pipeline {
    agent any
    environment {
        MLFLOW_TRACKING_URI = 'http://localhost:5000'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'pip install mlflow'
                sh 'sleep 120' // Simulate build time
                sh "python scripts/log_build_time.py ${BUILD_NUMBER}"
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
                sh 'sleep 300' // Simulate deploy time
                sh "python scripts/log_deploy_time.py ${BUILD_NUMBER}"
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