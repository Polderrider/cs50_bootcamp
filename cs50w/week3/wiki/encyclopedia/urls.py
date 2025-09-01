from django.urls import path
from . import views


app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name='index'),                        # index page
    path("<str:title>", views.get_title, name='get_title'),
    path("search/", views.search, name='search'),
    path("add/", views.add, name='add'),
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