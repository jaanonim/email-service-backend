# emailService backend 

## Instalation:
### Create and activate environment
Create and activate a virtual environment.
```
python3 -m venv venv
venv\Scripts\activate
```

### Install packets
```
pip install -r requirements.txt
```
### Setup .env file
You need to create .env file in it some sensetive data.
### Migration and sync the database
Create an initial migration for models, and sync the database for the first time.
```
manage.py makemigrations email_messages tasks groups emails users
manage.py migrate
```
### Start up a server
Start python server:
```
python manage.py runserver
```