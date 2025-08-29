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

Learnings:
{% url 'app_name.view_name' arg1 %}     arg1 should be passed without templating {{ arg1 }}
eg incorrect {% url 'app_name.view_name' {{ arg1 }} %}    

html: position <li> </li> around <a href="">
correct: <li><a href="{% url 'encyclopedia:get_title' entry %}">{{ entry }}</a></li> so that each list item contains a link (instead of a link containing a list item).
possible to do it the other way, because the browser's error-correction rules fix incorrect markup.
Reasons to het it right: CSS selectors (ul > li > a) may break. / Browsers may fix it differently / Future browser changes could make your “working” HTML stop working.

## Feature: 05.1 - Return link from wikipage to index page

## Feature: 06 - search bar
REqurieemnts
6.1 Search: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry. If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.

6.2 If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ```'ytho'```, then ```'Python'``` should appear in the search results.  Clicking on any of the entry names on the search results page should take the user to that entry’s page.

Pending
tweak wording of search result messages returned to user to improve UX

Completed
layout.html updated with sidebar etc
static_dir added to settings, static/css/styles.css added to project root, {% load static %} tag included in html pages
user search query exact match - matching wikipage.html returned
user search query partial match - list of article titles containing search query returned as list



Notes
search uses GET method to retrieve 
3 known options to add search form to support search functionality
    1. html forms   2. Django forms     3. Crispy forms

SearchResults.html needed for 6.2 copy wikipage


