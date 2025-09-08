from django.urls import path
from . import views


app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name='index'),                        
    path("<str:title>", views.get_title, name='get_title'),
    path("search/", views.search, name='search'),
    path("add/", views.add, name='add'),
    path("edit/<str:title>", views.edit, name='edit'),
    path("delete/<str:title>", views.delete, name='delete'),
    path("get_random_title/", views.get_random_title, name='get_random_title'),

    

]




# PAGES
# /encyclopedia/                        → index page
# /encyclopedia/Liverpool               → wiki page
# /encyclopedia/add                     → create new wiki page



# QUERIES
# /encyclopedia/search/?query=foo       → search view

""" 
setup a url for the new query or new page in urls
 """