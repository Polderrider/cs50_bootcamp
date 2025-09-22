from django.shortcuts import render
from .models import Listing

# Create your views here.
def index(request):
    listings = []
    # listings = ["product A", "product B"]

    return render(request, "auctions/index.html", {
        "listings": listings
    })