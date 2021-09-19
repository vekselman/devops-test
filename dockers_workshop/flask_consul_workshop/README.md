docker build --network nexus_nexus -t 127.0.0.1.nip.io/production/flask-api-consul:0.1 -f Dockerfile_multistage .

docker push 127.0.0.1.nip.io/production/flask-api:0.1