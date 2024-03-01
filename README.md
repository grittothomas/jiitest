# jiitest


 **Deployed Web Application URL**: (http://webappjiiecselb-132991313.us-east-1.elb.amazonaws.com/)

 **Web Service**: Python Flask

 **Containerization**: The web application has been containerized using Docker, and the Docker image has been pushed to Amazon ECR.

 **Cloud Platform**: AWS

 **CI/CD Implementation**: Jenkins

   - Jenkins has been configured to use Declarative Checkout SCM.
   - The code is automatically fetched from the GitHub repository.
   - The code is analyzed by Flake8.
   - Docker image is built and uploaded to Amazon ECR.
   - The application is deployed to Amazon ECS.
   - Jenkins server is hosted in an EC2 instance.
   - Required modules are specified in the requirements file for the web application.
   - Pipeline as Code is utilized for Jenkins configuration.

 **Dockerized App**: The web application is dockerized from the docker branch in the GitHub repository. 
