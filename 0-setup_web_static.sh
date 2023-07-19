#!/usr/bin/env bash
#!/usr/bin/env bash
#This bash script does the following
# 1) Install Nginix
# makes it listen on port 80
# points the 404 and /redirect me to specific locations

if ! command -v nginx &>/dev/null; then
	#installing Nginx Silently hence the dev null
	sudo apt -y install nginx > /dev/null
fi

#enable firewall
#sudo ufw allow 'Nginx HTTP'

#create dir if not existing / do nothing if existing
for dir in /data/web_static/{shared,releases/test}; do
    sudo mkdir -p "$dir"
done

# create fake file index
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
#creates a symbolic link
sudo ln -sf  /data/web_static/releases/test /data/web_static/current

#give folder ownership to ubuntu
sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# restart nginx service
sudo service nginx restart

echo "Script Complete"
