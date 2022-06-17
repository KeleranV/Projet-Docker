FROM alpine:latest

RUN apk update
RUN apk add nginx
RUN apk add openrc

RUN openrc
RUN touch /run/openrc/softlevel

RUN rc-update add nginx

VOLUME /home/server-9/projets/3/nginx/site /home/site:ro

RUN service nginx start

EXPOSE 80/TCP
ENTRYPOINT /bin/sh
