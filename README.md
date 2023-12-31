# codeforces.com parser + telegram bot
* Grabber collects data from codeforces.com to database
* Grabber check data updates on site every hour
* Telegram bot can request data from database (up to 10 values)
## Requirements
* Python
* Redis
* Postgres
## Project folders description
* [bot] - telegram bot configuration 
* [checker] - celery configuration
* [sql] - creation table query 
* [srq] - functional processing
* [tests] - pytest
* [img] - pictures for README
## Installation
* Download repo
* create virtual environment (python3 -m venv venv)
* activate virtual environment (source venv/bin/activate)
* Install requirements (pip install -r requirements.txt)
* Run service Redis (service redis-server start)
## Prepare 
* prepare database.ini file [postgresql] - connection to database [token] - bot secret token
* create database for postgres
* prepare telegram bot (you can use default configuration @codeforces_grabber_bot)
## Start service
* run command: celery -A checker beat --loglevel=INFO
* run command: celery -A checker worker --loglevel=INFO
* run python project (main.py)
* after first running and loading data from site you can work with bot
* run command /start in telegram bot
## Testing
Testing after creation databases (some test works with database)
* pytest --cov
* pytest --cov --cov-report html
 ## Examples work with interface
### cli menu
![img.png](img/img.png)
### main telegram bot menu
![img2.png](img/img2.png)
### telegram bot menu - search by difficult and theme
![img3.png](img/img3.png)
### telegram bot menu - search by title
![img4.png](img/img4.png)
## Additional
* Author: Avramenko Nikolay
* Date of release: 2023/09/17