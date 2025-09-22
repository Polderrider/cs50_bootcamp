from django.db import models

# Create your models here.

# ONE TO ONE
# a bid has only one user, one user has many bids
# one user has one watchlist, one watchlist has one user

# ONE TO MANY
# listing only has one user; one user has many listings

# MANY TO MANY
# one watchlist has many listings, one listing has many watchlists



# bid functionality -> listing.html button(place bid)input(currency) -> submit form(POST bid to bid table/class, render listing.html including bid table with latest bid)


# watchlist functinality -> listing.html -> button(add to watchlist) -> submit form(POST listing data) -> watchlist.html(message item added to watchlist class/table) -> 


class Listing(models.Model):
    
    # username = models.CharField(max_length=64)
    item_name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    # image = models.ImageField()
    # category = models.CharField(max_length=64)

    # date_created = models.DateField()



	