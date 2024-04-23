
# flask-login
flask-login
Deploying a Simple Flask App with kubernetes

## Creating docker Image
	 $ docker build -t registry.gitlab.com/mrhdavoodi/docker-images/flask-app:v1 .
	 $ docker push registry.gitlab.com/mrhdavoodi/docker-images/flask-app:v1

## Apply the Deployment
	  $ kubectl apply -f k8s-modules/backend-deployment.yaml

## Useful commands and Refs

	$ export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')" # Getting the port from the nodePort
	$ curl http://"$(minikube ip):$NODE_PORT" # service is publicly open to traffic
	$ k delete services $(k get services --output=jsonpath='{.items[*].metadata.name}')
#### Ref
 - https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/

