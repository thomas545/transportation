#!/bin/bash

source venv/bin/activate
pip install wheel
pip install -U pip

cd backend-app/
git pull
pip install -r requirements.txt 

sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
