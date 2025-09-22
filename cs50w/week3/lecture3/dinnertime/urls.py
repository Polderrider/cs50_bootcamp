from django.urls import path
from . import views

app_name = "dinnertime"
urlpatterns = [
    path("", views.dinnertime, name="dinnertime")
]