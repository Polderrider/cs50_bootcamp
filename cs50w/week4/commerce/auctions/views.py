from django.shortcuts import render
from .models import Listing

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

