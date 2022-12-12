pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git branch:main, url: 'https://github.com/sanjayganesh5/pythoncicd.git'
            }
        }
        stage('Install Coverage') {
            steps {
                sh 'pip install coverage'
            }
        }
        stage('Generate Coverage') {
            steps {
                sh 'python -m coverage run -m unittest test_calc.py'
                sh 'python -m coverage xml -o coverage.xml'
            }
        }
        stage ('Sonar Analysis') {
            environment {
                scannerHome = tool 'Sonar4.7'
            }
            steps {
                withSonarQubeEnv('Sonar') {
                    sh '''${scannerHome}/bin/sonar-scanner \
                    -Dsonar.projectKey=python-cicd \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://13.235.24.154 \
                    -Dsonar.login=fef7d56832a9261ccd0b9b5d39e7d35d0a1f741b \
                    -Dsonar.python.coverage.reportPaths=coverage.xml'''
                }
            }
        }
    }
}