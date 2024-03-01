pipeline {
    agent any

    environment {
        PATH = "/usr/bin:${env.PATH}"
        registryCredential = 'ecr:us-east-1:awscreds'
        appRegistry = "585331861466.dkr.ecr.us-east-1.amazonaws.com/jiitest"
        webappRegistry = "https://585331861466.dkr.ecr.us-east-1.amazonaws.com"
        cluster = "webapp-jiit"
        service = "webappjiisvc"
    }
  stages {
    stage('Fetch code'){
      steps {
        git branch: 'docker', url: 'https://github.com/grittothomas/jiitest.git'
      }
    }

  stage('Code Analysis - Flake8') {
              steps {
                  script {
                      sh 'flake8 .'
                  }
              }
              
          }
    
    stage('Run pytest') {
            steps {
                // Run pytest tests
                sh 'pytest'
            }
    }


    

    stage('Build App Image') {
       steps {
       
         script {
                dockerImage = docker.build( appRegistry + ":$BUILD_NUMBER",)
             }

     }
    
    }

    stage('Upload App Image') {
          steps{
            script {
              docker.withRegistry( webappRegistry, registryCredential ) {
                dockerImage.push("$BUILD_NUMBER")
                dockerImage.push('latest')
              }
            }
          }
     }

    stage('Deploy to ecs') {
          steps {
        withAWS(credentials: 'awscreds', region: 'us-east-1') {
          sh 'aws ecs update-service --cluster ${cluster} --service ${service} --force-new-deployment'
        }
      }
     }
  }
}