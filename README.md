# interacle_apy



Building your image and pushing it to hub.docker for later use

docker image build -t <name_image> .

docker tag <name_image>:latest <your_hub.docker>/<repo>:latest

docker push <your_hub.docker>/<repo>:latest



Using remote image to deploy a k8s solution



​	kubectl create namespace <your_namespace>

​	kubectl apply -f deployment.yaml -n <your_namespace>

​	kubectl apply -f service.yaml -n <your_namespace>

kubectl expose deployment <your_deployment> --port=5000 --type=<service_type>

Obs:Refer to [ Services ](https://kubernetes.io/docs/concepts/services-networking/service/ )to see service types



Fill in your credentials inside env.list

#builds your image
docker image build -t rcl_inte_api .

#runs docker parsing port, envs, setting a name and deatched mode
docker run -p 5000:5000 --env-file env.list --name client_intg_api -d

