FROM debian:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install certbot python3-certbot-dns-ovh python3-certbot-nginx -y

CMD [ "/bin/sh", "-c", "while true; do sleep 1; done" ]



