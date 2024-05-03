#!/usr/bin/env bash
# Prepare your web servers
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i 's,root \/var\/www\/html;,# root \/var\/www\/html;\n\tlocation hbnb_static {\n\t\talias /data/web_static/current/;\n\t},' /etc/nginx/sites-enabled/default
