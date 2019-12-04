FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.aliyun.com/g" /etc/apt/sources.list


RUN   apt-get -y update && \ 
      apt-get -y  install apache2 php-mysql php vim libapache2-mod-php  php7.0

RUN rm -rf /var/www/html/*
COPY phpinfo.php /var/www/html
COPY robots.txt /var/www/html
COPY index.html /var/www/html
COPY ./src /var/www/html/phpmyadmin

RUN echo gwctf{JUst_q_1I111l1Il11DAYS} > /flag
RUN chmod 444 /var/www/html

RUN chmod -R 444 /app

COPY ./start.sh /start.sh
RUN chmod +x /start.sh
EXPOSE 80

CMD ["/start.sh"]

