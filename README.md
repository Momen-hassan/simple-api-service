# Simple API Service 

## Overview This project is a simple Flask-based API deployed as a Docker container and managed via Helm on a Kubernetes cluster. It provides basic functionality to demonstrate a RESTful service.
 ## Prerequisites Before starting, ensure you have the following installed: - Docker - Kubernetes (Minikube or any Kubernetes cluster) - Helm 3 – Git 

 ## Getting Started 

## Building the Docker Image 1. **Navigate to the Project Directory:** Open a terminal and change to the project root directory. 
cd /home/batmo/simple-api-service

2. **Build the Docker Image:** Compile the Docker image from the Dockerfile. This image encapsulates the Flask application. 
docker build -t simple-api-service .
#TODO: Automate image version tagging to avoid using "latest" in a real situation. 
###Running the Docker Image Locally 1. **Run the Container:** Start the Docker container to test locally. This command maps port 5000 of the host to port 5000 of the container. 
docker run -p 5000:5000 simple-api-service

Access the Application

You can now access the service at http://localhost:5000/data.

The application exposes the following endpoints:

/data: Returns a simple JSON message.
/metrics: Returns Prometheus metrics.
/healthz: Liveness probe endpoint.
/ready: Readiness probe endpoint.
You can test these endpoints using curl:

curl http://localhost:5000/data
curl http://localhost:5000/metrics
curl http://localhost:5000/healthz
curl http://localhost:5000/ready

You can now access the service at http://localhost:5000/data.
 ### Deploying to Kubernetes with Helm 1. **Start Minikube:** If using Minikube for a local Kubernetes environment, start it with: 
minikube start
2. **Deploy Using Helm:** 
Ensure your Helm chart is updated with the correct image repository and tag:

image:
  repository: <your-docker-registry>/simple-api-service
  pullPolicy: IfNotPresent
  tag: "latest"

Deploy the application using Helm to manage the Kubernetes resources:
 
helm upgrade --install my-api-service /simple-api-service/api-service/

#TODO: Ensure Helm charts include resource limits and requests for production readiness. 
3. **Verify Deployment:** Ensure the service is correctly deployed: 
kubectl get deployments  
  kubectl get pods
**Watch for any issues, particularly with image pulling or probe configurations.(the cluster port in the values.yamlis runing on 8080 please make sure this port does not conflict to avoid any issues while pullingt the image and running the pod**
### Testing the Service To test the service after deployment: 1. **Access via Minikube:** Use Minikube 
minikube service my-api-service

Meaningful Comments
The git commits include meaningful comments to explain the changes made:

git add .
git commit -m "Updated application and Dockerfile"
git push origin main
