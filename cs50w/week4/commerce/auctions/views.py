from django.shortcuts import render
from .models import Listing

# Create your views here.
def index(request):
    

    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })