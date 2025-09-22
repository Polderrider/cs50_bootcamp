from django.urls import include, path
from . import views


app_name = "newyear"
urlpatterns = [
    path("", views.celebrate, name="celebrate"),
]