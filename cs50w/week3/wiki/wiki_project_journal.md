### Wiki Project Journal


A place to jot down notes, insights and thoughts that crop up while working on wiki project features.


## Feature 1 - Initialise Django Project 
21 August 2025

# completed
startproject - startapp - project/settings.py to recognise app urls - forgot to 'include' app.urls iin project.urls file.
app/urls.py urlpatterns & app name
app/views.py added index view
app/utils.py added placeholders for helper functions
app/templates/app added html placeholders for layout.html and index.html


does app run?
No. ModuleNotFoundError: No module named 'encyclopediadjango'
unsure how module ended up being named like this? Ans. forgot to add comma to seperate app name in INSTALLED APPS list in settings.py
2nd attempt = No. forgot to 'include' app.urls in project.urls file.
3rd attempt = Yes, encyclopedia app runs and displays placeholder html file.

tests
added one test for index view to confirm statuscode=200, and html rendering correctly

# pending
n/a


--------------------------------------------------------------------------------------------

## Feature 2 - Index View   

This view returns a template encyclopedia/index.html, providing the template with a list of all of the entries in the encyclopedia (obtained by calling util.list_entries, which we saw defined in util.py).

Assumptions:
the wiki entries list should be the same for all users visiting the site => use global varaible to hold list, rather than using request.session to hold a local view of the list which prevents user B or C seeing changes made to the list by User A. 
Question: can reqeust.session["entries"] = [] be used as a global list available to all users? Is it a cleaner way to work?