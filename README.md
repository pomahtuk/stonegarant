## ToDo list:

* Banners management in admin
* Ajax catalog loading
* review submission
* hover on memorial?

git remote add fastvps git@s052d7cc1.fastvps-server.com:stonegarant.git


http://python-rq.org/patterns/supervisor/

// queues
python manage.py rqworker high default low --burst
python manage.py rqscheduler

* Automated e-mail sending

Стэлла (120/60/8):
Длина 120 (это высота стелы)
Ширина 60 (это ширина)
Высота 8 (это толщина)

Цветник (120/60/8):
Длина 120
Ширина 60
Толщина 8

## Instalation:
    ALTER TABLE stonegarant_order MODIFY total_price bigint(20);
    alter table stonegarant_order modify podstavka_id int(11);
    alter table stonegarant_order modify cvetnik_id int(11);
    alter table stonegarant_order modify polirovka_id int(11);

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
