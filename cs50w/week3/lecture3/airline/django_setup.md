

1. django-admin startproject name       eg airline
2. create app folder name
3. cd app folder
4. python manage.py startapp app_name. eg flights

files 
1. settings.py -> add name of app to. list of INSTALLED_APPS

2. project level urls.py -> 
        map project urls to app urls by including in project "urlpatterns" list:
                path('flights/', include("flights.urls")),

3. app level urls.py
        map app to first page by adding path in app "urlpatterns=" list:
            path("index/", views.index, name=index)

        from . import views

4. add amodel / class
    advise django to setup a db 
    tell django to upudate db to add info about models.  do this by "migrate" command
    2 step process 1. create migration (instructions how to change db) 2. migrate apply instructions to db

    (note, set model and class up first)
    python manage.py makemigrations
    then
    python manage.py migrate
        

