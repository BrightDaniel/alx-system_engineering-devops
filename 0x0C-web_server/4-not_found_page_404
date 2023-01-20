#!/usr/bin/env bash
# Configure your Nginx server to have a custom 404 page

apt-get update
apt-get install -y nginx

mkdir /etc/nginx/html
touch /etc/nginx/html/index.html
echo "Hello World!" > /etc/nginx/html/index.html
touch /etc/nginx/html/404.html
echo "Ceci n'est pas une page" > /etc/nginx/html/404.html

printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
