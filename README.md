## Instalation:

### Python
	
    brew install python && pip install virtualenv
    mkdir ~/Virtualenvs && cd ~/Virtualenvs
    virtualenv stonegarant
    source stonegarant/bin/activate
    pip install -r requirements.txt

### MySQL
	mysql -u root stonegarant < dump.sql

### Migrations
    ./manage.py migrate stonegarant --fake-initial



## Running server:

	./manage.py runserver