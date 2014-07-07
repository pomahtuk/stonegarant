#!/bin/bash

NAME="memorial_app"                               				# Name of the application
DJANGODIR=/var/www/open_cook_web/data/www/stonegarant/  			# Django project directory
SOCKFILE=/var/www/open_cook_web/data/www/stonegarant/run/gunicorn.sock  	# we will communicte using this unix socket
NUM_WORKERS=3                                     				# how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=stonegarant.settings             			# which settings file should Django use


echo "Starting $NAME"

# Activate the virtual environment
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
#exec ./manage.py collectassets
exec gunicorn_django \
  --name $NAME \
  --workers $NUM_WORKERS \
  --log-level=debug \
  --bind=unix:$SOCKFILE

