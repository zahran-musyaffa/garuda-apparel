# Garuda Apparel
explain how to implement checklist above:
## Creating django project 
first i create directory named garuda-apparel then i create and open virtual environment `python -m venv env` `env\Scripts\activate`
then i create requirement.txt and install it by using `pip install -r requirements.txt` after that i create django project named `garuda_apparel`
add .env and .env.prod
modify settings.py
do migrate by `python manage.py migrate`
then start django server by "pythoon manage.py runserver"
## PWS configuration
make new project called "garuda apparel" then change the raw environment like .env.prod
then add allowed_host in settings.py after that build project using instruction in pws
## Setup main application 
add new app with name main by `python manage.py startapp main`
then register it in `INSTALLED_APPS` in settings.py
after that create templates directory and add main.html  file 
change models.py yhen do migration with `python manage.py makemigration` and `python manage.py migrate`
enter data in views.py and modify templates
then add urls.py file inside main folder then we import include 
## start project
run project using `python manage.py runserver`


## Explain role of settings.py
1. lists installed apps in INSTALLED_APPS
2. database configuration
3. security setting : Secret_key , Debug , allowed hosts

## How does database migration work in Django
every changes in models.py need to be migrated. migration work to similar databse with model wwe make in models.py. when changin models.py Django will make migration file with `python manage.py makemigrations`. after that to apply change to database by using `python manage.py migrate`

## Why Django framework chosen as starting point for learning software development
I think because Django already has many feature template, so students doesnt need to start from beginnning and go to software consept like MVT.

## Feedback for TA for Tutorial 1
none