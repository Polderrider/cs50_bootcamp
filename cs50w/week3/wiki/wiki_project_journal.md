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


# pending
tests