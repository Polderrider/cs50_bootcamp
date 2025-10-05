from django.db import models


# Create your models here.

# ONE TO ONE
# a bid has only one user, one user has many bids
# one user has one watchlist, one watchlist has one user

# ONE TO MANY
# listing only has one user; one user has many listings

# MANY TO MANY
# one watchlist has many listings, one listing has many watchlists




class Listing(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    item_name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    image = models.ImageField(upload_to="listing_images/", blank=True)
    
    
    
    
    # category = models.CharField(max_length=64)


    def __str__(self):
        return f'{self.id}: {self.item_name} Price: {self.price}'



	