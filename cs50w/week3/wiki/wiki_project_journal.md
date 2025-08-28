# Wiki Project Journal

Tracks progress on tickets noting milestones and insights that crop up working on project features.


## Feature 1 - Initialise Django Project 
21 August 2025

completed
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

pending
n/a


--------------------------------------------------------------------------------------------

## Feature: 02 - Index View   

have view.index return unordered list of entry names sourced from entries/
This view returns a template encyclopedia/index.html, providing the template with a list of all of the entries in the encyclopedia (obtained by calling util.list_entries, which we saw defined in util.py).

Assumptions:
dir named entries/ holds wikis as .md files -> in list_entries() function - use regex to scan entries/ for files ending in .md, return list of names as strs that can be displayed on index.html


--------------------------------------------------------------------------------------------

## Feature: 03 - markdown files displayed as html   

### learnt about
.glob()
.resolve().parent
filename.read_text() preferred way of reading text from a file if memory saving, don't need read one line at a time isn't important otherwise use context manager with open('filename.ext', 'r') as infile:
use pathlib and .glob() to search for "*.md" 
brew fd, fuzzy search +vs code. = code $(fd .md |  )


Regex file ext search/match
1. practice in standalone. use regex to return and print list of filenames in entries/
text = "filename.md"
match = re.match(r"([A-Za-z0-9_-]+)\.md", text)

Completed
| 3         | Entry Markdown Storage       | Store each entry as a Markdown (.md) file in a local `entries/` folder                       |
| 3         | Entry Markdown Retrieval     | Implement function to retrieve the Markdown content of an entry by title                     |
| 3         | Markdown to HTML Conversion  | Convert Markdown to HTML before rendering entry pages                                        |
| 3         | Entry Page View              | Create a dynamic route `/wiki/<title>` to display a specific entry 
| 3         | Entry Not Found Page         | Display error page when a requested entry does not exist    

Notes:
404.html sits in project/templates
404.html can still inherit from layout.html using Django’s templating system - key point file location in the directory matters not, as long as your template loader can find both files.
Gotcha: Ensure APP_DIRS=True or TEMPLATES['DIRS'] includes both the project-level and app-level templates/ directories.




## Feature: 04 - tests
pending
test 404 returned

completed
added tests for views to ensure status code 200 returned and md files correctly converted into html


## Feature: 05 - Index Page Links
add a link to each list entry shown on the index page which leads to the into a link to its respective html entry page 

Notes: 
use app_name = encyclopedia to access the namign convetion app_name:view name
use templating language {% url '' %}
add link inside templating language in  index.html


