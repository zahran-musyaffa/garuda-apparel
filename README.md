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

# Garuda Apparel - Assignment 3 

## Why do we need data delivery in implementing a platform?
Data delivery enables the exchange of information between different system components and servers. it allows platforms to communicate dynamically, updating content, and provide interactive design. 
without Data delivery platform would be static and needed to refresh frequently make it limited due to functionality and scalability

## Which is better, XML or JSON
In my opinion JSON is better than xml because:
1. JSON has simpler and more easy to read compared to xml
2. JSON is supported by Javascript make it easy to use directly in web browsers

## Purpose of `is_valid()` method in Django forms and why do we need it
The `is_valid()` method in Django forms is used to validate form data submitted by users. It checks for correct data types and required fields.
We needed `is_valid()` method to ensure data is consistent before processing it. So it will prevent error in database and in application.

## Why do we need `CSRF_token` when making forms in Django ? What happen when we dont include `csrf_token` in Django form ?
CSRF token is needed to protect our Django project from Cross-Site Request Forgery attacks. CSRF token is security mechanism that protects our website against malicious website performing unauthorized action
Without CSRF token: 
1. attackers could delete modify or create data.
2. check and change our personal privacy such as email, address, password and many our sensitive information

## Explain how to implement checklist above :
1. first i create templates folder and add `base.html` file. this file is used as a generic view for other web pages in this project. 
Then i add templates in `DIRS , templates` in `settings.py` so base.html recognize as templates file. After that i extend base.html in `main.html` file 
2.  After that in `main` directory add `forms.py` file to display and accept users input 
3. Creating views to displaying and adding data. Then use `is_valid()` to makesure users input meets all validation.
4. Add url routes to access each view
5. Build `html templates` for list form and detail_news
6. Add xml and JSON format to data delivery views
9. Adding xml and json url patterns for accessing XML and JSON data 
10. Adding to git and pws by using `git add-commit-push`

## Postman Screenshots
image.png

## Any feedback for teaching assistant
none 