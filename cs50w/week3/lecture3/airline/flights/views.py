from django.shortcuts import render
from django import forms
from .models import Airport, Flight, Passenger 
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class BookingForm(forms.Form):
    name = forms.CharField(max_length=64)
    surname = forms.CharField(max_length=64)


def index(request):
    """ displays a list of all flights """

    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
         
    })

def flight(request, flight_id):
    """ returns data for a single flight in response to a given flight_id """
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),      
        
        # Note, .passengers.all() is the "related-name" set in the Passengers class as part of the flights var which holds the manytomany relationship with Flgith class.
    })

def booking(request, flight_id):

    # post
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight) 

        return HttpResponseRedirect(reverse("flight", args=(flight_id,))) 

        # my work
        # form = BookingForm(request.POST)
        # name = form["name"]
        # surname = form["surname"]




    
