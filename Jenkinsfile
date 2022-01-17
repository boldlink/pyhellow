pipeline {
  agent any
  stages {
    stage('demo dummy Job') {
        agent {
          kubernetes { yamlFile "pod-cicd.yaml" }
        }
      steps {
          sh '''
            set +e
            echo "------------------Demo Job---------------------"
            terraform --version
            python3 version
            pip3 --version
            cd src
            pip3 install -r requirements.txt
            echo "------------------Demo Job---------------------"
          '''
        }
      }
    }
  }
