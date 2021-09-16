Steps to up jenkins of devops course 
```bash
sudo yum install git -y
git clone --branch advanced https://github.com/yanivomc/docker-cicd.git
cd docker-cicd

docker-compose -f docker-compose-jenkins.yml up
```
Browse: http://IP:8080/  
1. User:pass - admin:admin