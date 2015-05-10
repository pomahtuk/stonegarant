## ToDo list:

* Automated e-mail sending
* Require-js architecture


## Instalation:

### Python
	
    brew install python && pip install virtualenv
    mkdir ~/Virtualenvs && cd ~/Virtualenvs
    virtualenv stonegarant
    source stonegarant/bin/activate
    pip install -r requirements.txt

### MySQL
    
	mysql -u root stonegarant < dump.sql
	ALTER TABLE stonegarant_reply CHANGE preson person VARCHAR(50);

### Migrations

    ./manage.py migrate stonegarant --fake-initial


## Running server:

	./manage.py compress && ./manage.py runserver