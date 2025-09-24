from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Listing
from django import forms
from django.urls import reverse

class CreateListingForm(forms.Form):
    item_name = forms.CharField(max_length=64)
    description = forms.CharField(max_length=64)
    price = forms.IntegerField()
    image = forms.ImageField()

# Create your views here.
def index(request):
    """ returns all listings to the index page """

    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })

def listing(request, listing_id):
    """ returns a single listing with details in response to a given id:int """

    listing = Listing.objects.get(pk=listing_id)
    
    return render(request, "auctions/listing.html", {
        "listing": listing
    })

def create(request):
    """ returns an empty form (GET) or returns listing data (POST) from completed form """

    if request.method == "POST":
        form = CreateListingForm(request.POST, request.FILES)
        if form.is_valid():
            item_name = form.cleaned_data["item_name"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            image_file = form.cleaned_data["image"]

            listing = Listing(
                item_name=item_name, 
                description=description, 
                price=price, 
                image=image_file)
            
            listing.save()
            return HttpResponseRedirect(reverse("auctions:listing", args=(listing.id,))) 

    # GET render an empty CreateListingForm
    form = CreateListingForm()
    return render(request, "auctions/create.html", {
        "form": form
    })







