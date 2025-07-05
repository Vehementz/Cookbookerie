In create-charts folder : 
```
helm template nginx
```


The config store helm chart has been created with that command 
```
helm create config-store
```

```
kubectl get pod -n kube-system
```


```
helm lint config-store
```

```
helm template config-store
```


```
helm install config-store config-store # require the database 
```

```
kubectl logs config-store-<pod-id>
```

```
kubectl get deploy,svc,pod
```

```
helm repo list
```

```
helm repo update
```

```
helm search repo postgresql
```


Need to do it in `config-store` folder
```
helm dependency update
```


```
helm template .
```



```
kubectl create secret generic postgres-creds --from-env-file=.env
```


```
kubectl get secret
```

```
kubectl describe secret postgres-creds
```


