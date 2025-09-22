from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Listing
from django import forms
from django.urls import reverse

class CreateListingForm(forms.Form):
    item_name = forms.CharField(max_length=64)
    description = forms.CharField(max_length=64)
    price = forms.IntegerField()

# Create your views here.
def index(request):
    """ returns all listings to the index page """

    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })

def listing(request,  listing_id):
    """ returns a single listing with details in response to a given id:int """

    listing = Listing.objects.get(pk=listing_id)
    
    return render(request, "auctions/listing.html", {
        "listing": listing
    })

def create(request):
    """ returns an empty form (GET) or returns listing data (POST) from completed form """

    if request.method == "POST":

        
        name = request.POST["item_name"]
        description = request.POST["description"]
        price = int(request.POST["price"])

        listing = Listing(item_name=name, description=description, price=price)
        listing.save()
       

        return HttpResponseRedirect(reverse("listing", args=(listing.id,))) 



    # GET render an empty CreateListingForm
    form = CreateListingForm()
    return render(request, "auctions/create.html", {
        "forms": form
    })







