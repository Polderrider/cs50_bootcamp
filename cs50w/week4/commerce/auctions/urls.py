from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),                            #  auctions/.           shows index view which renders index.html
    path("<int:listing_id>", views.listing, name="listing"),        #  auctions/listing_id  shows listing view which renders listing.html with listing_id details
    path("create/", views.create, name="create"), 
]