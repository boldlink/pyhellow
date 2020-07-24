# pyHelloW
[![Build Status](https://drone.tools.boldlink.io/api/badges/boldlink/pyHelloW/status.svg)](https://drone.tools.boldlink.io/boldlink/pyHelloW)

Python RestAPI for demo testing and creating platforms while development is still underway

The output you should get is:
```json
{
  "hostname": "pyhellow-api-xxxxxxxx-xxxxxx",
  "greeting": "Hello World",
  "now": "Fri, 24 Jul 2020 09:55:54 GMT"
}
```
If the OS Env variable `HOSTNAME` isn't set your request will be:
```json
{
  "greeting": "Hello World",
  "now": "Fri, 24 Jul 2020 09:55:54 GMT"
}
```
## Running your Application

### Local command line
```
$ python3 src/main.api
```

### Kubernetes

#### Client Prerequisites:
* Python 3
* minikube
* kubectl
* helm version 3.x.x
* git 
* curl

#### AWS Prerequisites:
* EKS Cluster
* RBAC enabled
* Metrics server

### Run on Minikube
Add helm repo
```
$ helm repo add pyhellow https://boldlink.github.io/pyhellow/charts/

$ helm repo update
```
Install the app
```
$ kubectl --context minikube create ns pyhellow

$ helm install pyhellow-api pyhellow/pyhellow-api --kube-context=minikube -n pyhellow
```
Navigate service
```
$ minikube service pyhellw-api --url

$ curl http://http://192.168.99.100:31252/v1/api
```
Upgrade the app
```
$ helm install pyhellow-api pyhellow/pyhellow-api --kube-context=minikube -n pyhellow
```
### Run on EKS
Add helm repo
```
$ helm repo add pyhellow https://boldlink.github.io/pyhellow/charts/
$ helm repo update
```
Make sure your eks config is up-to-date
```
$ aws eks update-kubeconfig --name CLUSTER_NAME
```
Install the app
```
$ kubectl create ns pyhellow
$ helm install pyhellow-api pyhellow/pyhellow-api -n pyhellow
```
Navigate to the service
```
$ kubectl get svc

# Add /vi/api to curl
$ curl http://http://xxxxxxxxx-xxxxxx.xx-xxxx-x.elb.amazonaws.com:31252/v1/api
```
Ugrade the app
```
helm upgrade pyhellow-api pyhellow/pyhellow-api -n pyhellow
```
## Drone CI pipeline
A demo pipeline was added as well configured for our environment, it includes the following steps:
* [github]: Run Superlinter to validate code syntax
* [drone]: SonarCube scanner for code analysis
* [drone]: Scan image with Clair
* [drone]: Build and push docker image
* [drone]: Deploy helm chart to dev
* [drone]: Deploy helm chart to prod