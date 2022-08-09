pipeline {
    agent any
    stages {
    stage('testing binary search') {
      steps {
        echo 'testing binary search...'
        bat 'python binary_search.py'
      }
    }

    stage('testing bubble sort') {
      steps {
        echo 'testing bubble sort...'
        bat 'python bubble_sort.py'
      }
    }
    
     stage('testing quick sort') {
     steps {
       echo 'testing quick sort...'
       bat 'python quick_sort.py'
     }
   }
      
     stage('testing selection sort') {
     steps {
       echo 'testing selection sort...'
       bat 'python selection_sort.py'
     }
   }

  }

}
