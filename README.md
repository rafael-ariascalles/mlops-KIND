# mlops-KIND
Kubernets in Docker setup and MLOps practices

# Pre-requisites
go
docker
docker-compose
kubectl

## Hardware requirements in virtual machine
4 CPU / 8 GB RAM

# Setup
if docker is not running, start docker
```bash
sudo service docker start
```
test Docker
```bash
docker run debian sleep 5
```

dowload KIND from https://github.com/kubernetes-sigs/kind/releases/

for Linux OS:
```bash
wget -O kind https://github.com/kubernetes-sigs/kind/releases/download/v0.17.0/kind-linux-amd64
chmod u+rwx kind
sudo mv ./kind /usr/local/bin/kind
```
configuration of kubectl context
```bash
kubectl config set current-context --namespace=default kind-class
 ```   

Have all the information to connect to the cluster
```bash
kubectl config view --minify
```

show the kubelet process running inside the container class-control-plane
```bash
docker top class-control-plane | grep /usr/bin/kubelet
```

Critical pieces of information:
kube-apiserver (gatekeeper)
and in master node
```bash
docker top class-control-plane | grep kube-apiserver
```

kubectl get deployment -n default
kubectl get replicaset -n default
kubectl get pods -n default

kubectl port-forward <POD_NAME> <PORT>


if we want to test the api server
```bash
kubectl proxy --port=8080
```
from the repo
git clone https://github.com/spkane/class-kind-manifests.git     --config core.autocrlf=input


using for ingress and adding nodeports
```bash
kind create cluster --name class --config=ingress.yaml
```
















### just in case

Go
```bash
wget https://go.dev/dl/go1.19.3.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.19.3.linux-amd64.tar.gz
```
add to .bashrc
```bash
export PATH=$PATH:/usr/local/go/bin
```
test Go
```bash
go version

export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH

```
