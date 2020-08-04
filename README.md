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

$ helm install pyhellow-api pyhellow/pyhellow-api -f charts/values-mini.yaml --kube-context=minikube -n pyhellow
```
Navigate service
```
$ minikube service pyhellw-api --url

$ curl http://192.168.99.100:31252/v1/api
```
Upgrade the app
```
$ helm upgrade pyhellow-api pyhellow/pyhellow-api -f charts/values-mini.yaml --kube-context=minikube -n pyhellow
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
$ helm install pyhellow-api pyhellow/pyhellow-api -f charts/values-aws.yaml -n pyhellow
```
Navigate to the service
```
$ kubectl get svc

# Add /vi/api to curl
$ curl http://xxxxxxxxx-xxxxxx.xx-xxxx-x.elb.amazonaws.com:31252/v1/api
```
Ugrade the app
```
helm upgrade pyhellow-api pyhellow/pyhellow-api -f charts/values-aws.yaml -n pyhellow
```
## CI/CD pipeline
A demo pipeline was added as well configured for our environment, it includes the following steps:
* github: Run Superlinter to validate code syntax
* drone: SonarCube scanner for code analysis
* drone: Build and push docker image
* drone: Scan image with Clair
* drone: Deploy helm chart to dev
* drone: Deploy helm chart to prod

## The helm repo and chart
This github repo is also the Helm repo, bellow are the commands helm chart related (Yes still manual)

##### Prepare Helm chart
```shell script
$ cd charts/
$ helm lint helm-chart-sources/*
```
##### Package
```shell script
$ helm package pyhellow-api/
```
##### Update the repo index
```shell script
$ helm repo index --url https://boldlink.github.io/pyhellow/charts/ --merge index.yaml .
```
Commit the changes and have fun :)