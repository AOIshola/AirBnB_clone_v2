#!/usr/bin/env bash
# Prepares web server for deployment of web static

if ! dpkg -l nginx | grep -E 'ii.*nginx' > /dev/null 2>&1;
then
        sudo apt update
        sudo apt -y install nginx
else
        echo "Nginx already installed"
fi

# Create the folder /data/ if it doesn’t already exist
sudo mkdir -p /data

# Create the folder /data/web_static/ if it doesn’t already exist
sudo mkdir -p /data/web_static/

# Create the folder /data/web_static/releases/ if it doesn’t already exist
sudo mkdir -p /web/web_static/releases

# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html
sudo touch /data/web_static/releases/test/index.html

# Create web content
echo "<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Test web page</title>
</head>
<body>
    <h1>Testing A.O.Ishola's web server</h1>
    <footer>
        <h3>Goodbye User</h3>
    </footer>
</body>
</html>" | sudo tee "/data/web_static/releases/test/index.html" > /dev/null

sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static

nginx_config_file="/etc/nginx/sites-available/default"
web_static_path="/data/web_static/current"

echo "
server {
        listen 80;
        listen [::]:80;

        server_name _;

        location /hbnb_static {
                alias $web_static_path;
                index index.html;
        }
}" | sudo tee "$nginx_config_file" > /dev/null;

# test nginc configuration
sudo nginx -t

# restart nginx
sudo service nginx restart
