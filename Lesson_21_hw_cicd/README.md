CI_CD MSA Essentials pages 71-88  

#### Run following docker command
```bash
docker-compose -f /home/leonid/devops-test/Lesson_21_hw_cicd/docker-compose-jenkins.yml up
```

#### Create self signed certificates
```bash
openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out devopsstudy.nip.io.crt \
            -keyout devopsstudy.nip.io \
            -subj "/C=IL/ST=Bat Yam/L=Bat Yam/O=devops_study/OU=Devops/CN=devopsstudy.nip.io/emailAddress=leonid.gaidai1989@gmail.com"
```