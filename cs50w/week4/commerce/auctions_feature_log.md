# Auctions Site - Feature Log

Create an auctions site.  
Site shows a list of products that are being auctioned on main page.
Users need to create an account and login in order to create a new auction for a product
clikcing on product area navigates to a product_listing page

# bid functionality -> listing.html button(place bid)input(currency) -> submit form(POST bid to bid table/class, render listing.html including bid table with latest bid)
# watchlist functinality -> listing.html -> button(add to watchlist) -> submit form(POST listing data) -> watchlist.html(message item added to watchlist class/table) -> 





## Feature Log

| Feature # | Feature Name                 | Description                                                                                                              |
|-----------|------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| initial   | Project Setup                | Initialize Django project and app, create required folders and basic templates                                           |
| initial   | Index View                   | Render the index page with a list of encyclopedia entries (static placeholder list for now)                              |
| 1         | Listing model + index.html   | A listing model holds listings details submitted in shell and displays in simple list format on index.html               |
| 2         | Listing.html page            | use listing_id to navigate to listing.html to display basic information about a single product.                          |

| 3.0       | create new listing            |  add form to submit details (name, desc, price) to                          |
| 3.1       | views.create GET and POST     |  add http route functionality for GET (empty form) and POST (submit listing details)                        |
| 3.2       | create.html page.             |  html form method="post" for submitting listing data                                |


| 3.3         | update listing model- img,date |  expand Listing model to accept date and image                  |




                  