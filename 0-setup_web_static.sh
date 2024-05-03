#!/usr/bin/env bash
# Prepare your web servers
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i 's/listen 80 default_server/a \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t},' /etc/nginx/sites-enabled/default
sudo service nginx restart
