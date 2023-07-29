#!/bin/bash

sudo apt update
sudo apt-get install libsndfile1
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv nginx

# Make python env and clone project

python3 -m venv venv
source venv/bin/activate
pip install wheel
pip install -U pip

git clone https://github.com/thomas545/transportation.git
pip install -r transportation/requirements.txt

# Gunicorn conf

sudo cp transportation/deployment/gunicorn.service /etc/systemd/system/
cd /var/log/
sudo mkdir gunicorn
cd gunicorn/
sudo touch access.log
sudo touch error.log

cd
sudo chmod 777 /var/log/gunicorn/access.log
sudo chmod 777 /var/log/gunicorn/error.log

sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl restart gunicorn
sudo systemctl status gunicorn

echo "Gunicorn installed"

# Nginx conf

sudo cp transportation/deployment/nginx_dev /etc/nginx/sites-available/transportation
sudo ln -s /etc/nginx/sites-available/transportation /etc/nginx/sites-enabled

sudo openssl req -x509 -nodes -days 358000 -newkey rsa:2048 -keyout /etc/ssl/private/transportation.key -out /etc/ssl/certs/transportation.crt

sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'

sudo systemctl status nginx


echo "Nginx installed"


sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx

sudo systemctl status gunicorn
sudo systemctl status nginx

echo "Installation Done"
