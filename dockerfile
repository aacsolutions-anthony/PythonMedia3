FROM debian:latest 

RUN apt-get update && \
    apt-get install -y apache2 apache2-dev vim wget gcc python3-dev python3-pip 

RUN pip3 install mod_wsgi 

RUN mod_wsgi-express install-module >> /etc/apache2/mods-available/wsgi.load

RUN a2enmod wsgi 

COPY ./app /var/www/app

WORKDIR /var/www/app

RUN pip3 install -r requirements.txt

COPY ./app.conf /etc/apache2/site-available/app.conf 

RUN a2ensite app $$ a2dissite 000-default 

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
EXPOSE 8088

