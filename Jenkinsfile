pipeline {
    agent any

    stages {
        stage('Pre-check Docker') {
            steps {
                script {
                    echo "Checking if Docker is available on this agent..."

                    // Check Docker; if not available, fail clearly
                    def status = sh(script: 'docker info > /dev/null 2>&1', returnStatus: true)
                    if (status != 0) {
                        error """
Docker is NOT available on this Jenkins agent.
Please install Docker and ensure the Jenkins user can run Docker commands.
                        """
                    }
                    echo "Docker is available."
                }
            }
        }

        stage('Checkout') {
            steps {
                // Uses repo config from Jenkins job (GitHub SCM)
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: routepulse1-svc:4"
                sh 'docker build -t routepulse1-svc:4 .'
            }
        }

        stage('Run Container') {
            steps {
                echo "Stopping existing routepulse1-svc container (if any)..."
                sh '''
                    if [ "$(docker ps -aq -f name=routepulse1-svc)" ]; then
                        docker rm -f routepulse1-svc
                    fi

                    echo "Starting new container routepulse1-svc on port 12144..."
                    docker run -d --name routepulse1-svc -p 12144:12144 routepulse1-svc:4

                    echo "Currently running containers:"
                    docker ps
                '''
            }
        }
    }
}
