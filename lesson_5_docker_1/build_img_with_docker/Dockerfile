FROM ubuntu:18.04
RUN apt-get update && apt-get install apache2 -y && apt-get clean
COPY html /var/www/html
ENTRYPOINT ["apache2ctl", "-DFOREGROUND"]
