pipeline {
  agent any
  options {
    skipStagesAfterUnstable()
  }
  stages {
    stage('Pre-build') {
      steps {
        sh 'echo Pre-build!'
      }
    }
    stage('Build') {
      steps {
        sh 'echo Building...'
      }
    }
    stage('Post-build') {
      steps {
        sh 'echo Post-build!'
      }
    }
  }
}
