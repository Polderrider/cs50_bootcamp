
from django.db import models

# Create your models here.


class Airport(models.Model):

    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"



class Flight(models.Model):
     
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # placeholder for ManyToManyField relationship with PassengerClass (models.ManyToManyField(Flight)

    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination}'


class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    # necessary to model the fact that a flight has multiple passengers, and one passenger can take multiple flights -> .ManyToManyField, blank (ie a passenger can have no flights)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first_name} {self.surname}"




    
    

    
    