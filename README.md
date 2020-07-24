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
If the OS Env variable isn't set your request will be:
```json
{
  "greeting": "Hello World",
  "now": "Fri, 24 Jul 2020 09:55:54 GMT"
}
```
## Running your Application

### Local command line
```shell script
$ python3 src/main.api
```

### Kubernetes

#### Client Prerequisites:
* Python 3
* minikube
* kubectl
* helm version 3.x.x
* git 

#### AWS Prerequisites:
* EKS Cluster
* RBAC enabled
* Metrics server

### Run on Minikube
Add helm repo
```shell script
$ python3 src/main.api
```
