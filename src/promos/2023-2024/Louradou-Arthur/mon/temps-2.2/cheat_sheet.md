---
layout: layout/mon.njk

title: "Cheatsheet Kubernetes"
authors:
  - Arthur Louradou

date: 2024-01-17

tags: 
  - "temps 2"
  - "kubernetes"
  - "devops"
---


*Une fois l’installation de minikube faite avec Docker, voici les commandes utiles pour setup un nouveau projet, couplées avec les configurations de base pour lancer une app web avec une base de données MongoDB.*

```bash
minikube start --driver=none 
```

Sur Ubuntu, `--driver=qemu` fonctionne, `--driver=docker` aussi, à condition de rentrer dans `newgrp docker`

## Commandes

Après la configuration, voilà les commandes à disposition si les fichiers de configuration sont déjà prêts (`fichier.yaml` désigne les fichiers configmap, secret, deployment, service…) :

```bash
kubectl apply -f fichier.yaml
kubectl get pod
kubectl get services
kubectl get all
kubectl logs <nom du service dans get pods> # pour afficher les logs du container
kubectl describe pod <nom du service dans get pods> # pour corriger certains bugs

minikube ip # afficher l'ip de sortie
kubectl get node -o wide # alternantive sans minikube
```

## Fichiers de configuration

### ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mongo-config
data:
  mongo-url: mongo-service
```

### Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mongo-secret
type: Opaque
data:
  mongo-user: YWRtaW4=
  mongo-password: YWRtaW4=
```

<aside>
⚠️ Dans le pod MongoDB, il doit figurer la base64 des mots de passes et user sous peine d’erreur !

</aside>

### Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo-deployment
  labels:
    app: mongo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
      - name: mongodb
        image: mongo:5.0.23
        ports:
        - containerPort: 27017 # à reférencer dans les targetPort
        env:
        - name: MONGO_INITDB_ROOT_USERNAME
          valueFrom:
            secretKeyRef:
              name: mongo-secret
              key: mongo-user
        - name: MONGO_INITDB_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mongo-secret
              key: mongo-password
```

Pour ajouter des variables d’environnement au déploiement :

```yaml
spec:
  containers:
  - name: envar-demo-container
    image: gcr.io/google-samples/node-hello:1.0
    env:
    - name: DEMO_GREETING
      value: "Hello from the environment"
    - name: DEMO_FAREWELL
      value: "Such a sweet sorrow"
```

Ces variables seront considérées comme des variables de la ligne du dockerfile contenant “ENV”

```
ENV MONGO_DB_USERNAME=admin MONGO_DB_PWD=password
```

### Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mongo-service
spec:
  selector:
    app: mongo
  ports:
    - protocol: TCP
      port: 27017 # quelconque
      targetPort: 27017 # lié au containerPort
```

```yaml
apiVersion: v1
kind: Service
metadata:
  name: webapp-service
spec:
  type: NodePort
  selector:
    app: webapp
  ports:
    - protocol: TCP
      port: 3000 # quelconque
      targetPort: 3000 # lié au containerPort
      nodePort: 30100 # port ouvert sur l'extérieur avec l'ip du NodePort
```

<aside>
💡 Il est possible de mettre deux configurations (Deployment et Service par exemple) dans le même fichier en les séparant selon la syntaxe yaml : `---` sur une nouvelle ligne.

</aside>
