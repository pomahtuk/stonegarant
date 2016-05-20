#!/bin/bash

error_exit ()
{
  echo "$1" 1>&2
  exit 1
}

git --work-tree=/var/www/stonegarant --git-dir=/var/git/stonegarant.git checkout -f
cd /var/www/stonegarant || error_exit "error changing directory!. now exiting..."
echo "Switching to correct virtualenv..."
source /var/www/stgenv/bin/activate
echo "Installing dependencies..."
pip install -r requirements.txt || error_exit "error running pip install! now exiting ..."
echo "Applying migrations dependencies..."
./manage.py migrate stonegarant && ./manage.py migrate banners || error_exit "error rmigrating modelsl! now exiting ..."
echo "Collecting static files dependencies..."
./manage.py collectstatic --noinput || error_exit "error collecting static! now exiting ..."
echo "Restarting server..."
