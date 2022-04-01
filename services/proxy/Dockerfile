FROM ubuntu

RUN apt-get update -y && \
        apt-get upgrade -y && \
        apt-get install -y nginx && \
        apt-get install openssl -y

COPY ./ssl/ ./etc/nginx/ssl/
COPY ./conf.d/ ./etc/nginx/conf.d/
COPY ./default ./etc/nginx/sites-enabled/default
COPY ./html/ ./etc/nginx/html/


EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]