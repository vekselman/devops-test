```bash
docker run --rm -tdi \
--name web_api \
-p 8080:8080 \
-v /mnt/c/Users/user/IdeaProjects/seminars/docker/artifacts:/app \
java:openjdk-8-jre-alpine java -jar -Dspring.profiles.active=none /app/spring-music.jar 
```