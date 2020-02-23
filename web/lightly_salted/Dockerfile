FROM actilis/httpd-cgi:alpine-3.7 

RUN apk --no-cache add python3 && rm /var/www/html/index.sh /var/www/html/index.py
COPY lightsalt.py /var/www/html/index.sh


EXPOSE 80/tcp

