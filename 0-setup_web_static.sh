#!/usr/bin/env bash
# set up my web servers for the deployment of web_static 
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R www-data:www-data /data

sudo sed -i '/^\s*server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart

exit 0

