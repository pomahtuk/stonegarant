## Instalation:

### Python
	
    brew install python && pip install virtualenv
    mkdir ~/Virtualenvs && cd ~/Virtualenvs
    virtualenv stonegarant
    source stonegarant/bin/activate
    pip install -r requiremenys.txt
	

### MySQL
	mysql -u root stonegarant < dump.sql


## Running server
    ./manage.py migrate stonegarant --fake-initial

	./manage.py runserver