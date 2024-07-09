Apply the deployment from the deployment.yaml : 
```
kubectl apply -f=deployment.yaml
```

```
kubectl apply -f service.yaml
```
kubectl get services



kubectl get deployments

kubectl get pods



```
kubectl create deployment first-app --image=i1,i2,i3
```

```
kubectl expose deployment first-app --port=... --type=LoadBalancer
```

