tutorial docs: https://www.django-rest-framework.org/tutorial/quickstart/

api = application programming Interface 

# REST_FRAMEWORK Set up

step 1 -
- activate venv
-$pip install django
-$pip install djangorestframework

step 2
- django-admin startproject
- py manage.py startapp 

step 3 
- register app in settings 



step 4: 
- add superuser to DB $python manage.py createsuperuser --username admin --email admin@example.com

step 5
- in project/app create and populate the serializers.py 



# PREPARATION for DEPLOYMENT: 

step 1: 
- create .env file and $pip install django-dotenv

step 2: 
- move sensitive data to env file and use os.getenv('var_name') to use value

step 3: 
- move all static files to Static folder by using  $py manage.py collectstatic
- notice a new file called static appear in directory

step 4: 

