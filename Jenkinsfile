pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Abhilash319/employee-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-app:v1 .'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh 'docker rm -f employee-container || true'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker run -d \
                -p 5000:5000 \
                --name employee-container \
                employee-app:v1
                '''
            }
        }

    }
}