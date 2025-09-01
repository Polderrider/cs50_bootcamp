from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from . import util
from django import forms
from pathlib import Path
from django.contrib import messages



class NewWikipageForm(forms.Form):
    """ inheits form templating from Form to create user form for adding new entry """
    
    title = forms.CharField(label="Article Title", max_length=30)
    content = forms.CharField(label="Content", widget=forms.Textarea, max_length=500, )
    


def index(request):
    """ returns a list of article titles to display on the landing page """

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_title(request, title):
    """ return article content to wikipage for a given title """
    
    try:
        html_page = util.get_entry(title.lower())
    except FileNotFoundError:
        raise Http404

    return render(request, "encyclopedia/wikipage.html", {
        "html_page": html_page
    })
""" get_object_or_404 == Http404
from django.shortcuts import get_object_or_404


def my_view(request):
    obj = get_object_or_404(MyModel, pk=1)
This example is equivalent to:

from django.http import Http404


def my_view(request):
    try:
        obj = MyModel.objects.get(pk=1)
    except MyModel.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
"""


def search(request):
    """ extracts the user's submittted query term from request object in order to return a wikipage matching the query term exactly, or a list of wikiepage titles that contain the user's query """
    
    # get user's query from request originating from html form input
    query = request.GET["query"].strip()    # or query = request.GET.get("query", "").strip()
    if not query:
        return redirect("encyclopedia:index")
    # return list of articles on file
    articles = util.list_entries()
    
    exact_match = None
    for article in articles:
        if article.lower() == query.lower():
            exact_match = article
            break
    
    # article exists
    if exact_match:
        return redirect("encyclopedia:get_title", title=exact_match)    
    
    # article titles which contai search query
    similar = []
    for article in articles:
        if query.lower() in article.lower():
            similar.append(article)

    return render(request, "encyclopedia/search_results.html", {
        "similar": similar,
        "query": query
        
    })


def add(request):

    # POST data submitted to form
    if request.method == 'POST':
        form = NewWikipageForm(request.POST)
        
        # form data valid
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # check for duplicate title
            articles = util.list_entries()
            
            # list_entries() returns canoical titles (case sensitive), so article.lower() == title.lower()
            duplicate = False
            for article in articles:
                if article.lower() == title.lower():
                    duplicate = True
                    break
            # one liner using a generator to step through list. Stops at first match (eg break)
            # duplicate = any(article.lower() == title.lower() for article in util.list_entries())

            if duplicate:
                messages.error(request, f'An article titled "{title}" already exists. Choose a different title.')
                return render(request, "encyclopedia/add.html", {
                    "form": form,
                })
            
            # save content as new md file
            here = Path(__file__).resolve().parent
            util.save_entry(title, content, here)
                
            return redirect("encyclopedia:get_title", title=title)

        # form data not valid
        else: 
            return render(request, "encyclopedia/add.html", {
            "form": form,
        })
    
    # new empty form
    return render(request, "encyclopedia/add.html", {
        "form": NewWikipageForm()
    })
    


    return render(request, "encyclopedia/add.html")

    # output: markdown file 
    #       <- write user data to markdown file in dir /entries/ 
    #           <- open new markdown file <- read user data from request.POST into a variable 
    #               <- check form data .is_valid(), {% crsf_token %} security,  
    #                   <- capture user data in add.html form and POST to server
    #                       <- create 
    
    # create new instance of NewWikipageEntry


    # check form data .is_valid(), {% crsf_token %} security,

    # open new markdown file <- read user data from request.POST into a variable 
    
    # write user data to markdown file in dir /entries/ 


    