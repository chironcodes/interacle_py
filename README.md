# interacle_apy



This MVP solution longs to integrate an Oracle database. The project fetches data through SQL queries and feeds through a Rest API so it can be consumed.

Even though it's possible to use Model with flask, it was designed to fetch only specific columns and that we cannot do with ORM.

For the moment headers/tokens/auth will be hard coded as it'll be integrated with our cloud solution.
</br>
</br>

If you intend to test it locally, you should unzip **instantclient-basic*.zip** and export its path as *LD_LIBRARY_PATH*.

</br>

---
</br>
</br>
</br>

Building your image and pushing it to hub.docker for later use

```bash
docker image build -t <name_image> .

docker tag <name_image>:latest <your_hub.docker>/<repo>:latest

docker push <your_hub.docker>/<repo>:latest
```



You can deploy the API as a single docker container. To achieve this, you should fill in your credentials on **env.list** file and deploy it like this:

```bash
docker run -d -p 5000:5000 --env-file env.list --name integrate_me <your_hub.docker>/<repo>:latest
```



## Using remote image to deploy a Kubernetes solution:

If you intend to use it with k8s you should fill in your credentials inside the **Deployment.yaml** file before taking the next steps



```bash
kubectl create namespace <your_namespace>

kubectl apply -f deployment.yaml -n <your_namespace>

kubectl apply -f service.yaml -n <your_namespace>

kubectl expose deployment <your_deployment> --port=5000 --type=<service_type>
```

Refer to [ Services ](https://kubernetes.io/docs/concepts/services-networking/service/ )to see service types







