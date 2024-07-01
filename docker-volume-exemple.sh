#! /bin/bash
docker network create nginx_volume

docker run -d \
  --name nginxquest \
  -p 80:80 \
  -v nginx_volume:/usr/share/nginx/html \
  nginx:latest

# Wait for the container to fully start
echo "Waiting for Nginx to start..."
sleep 8

docker exec -i nginxquest sh -c 'echo "<h1>Bienvenue sur mon serveur Nginx !</h1>"  > /usr/share/nginx/html/index.html'
sleep 2
curl http://localhost:80
