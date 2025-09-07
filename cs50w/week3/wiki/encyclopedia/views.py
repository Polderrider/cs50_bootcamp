from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from . import util
from django import forms
from pathlib import Path
from django.contrib import messages



class WikipageForm(forms.Form):
    """ inheits form templating from Form to create user form for adding new entry """
    
    title = forms.CharField(label="Article Title", max_length=30)
    content = forms.CharField(
        label="Content", 
        widget=forms.Textarea(attrs={"rows": 40, "cols": 100}), 
        max_length=5000, 
    )
    


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
    # print(html_page)
    return render(request, "encyclopedia/wikipage.html", {
        "html_page": html_page,
        "title": title
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
        form = WikipageForm(request.POST)
        
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
        "form": WikipageForm()
    })
    


def edit(request, title):
    """ 
    accepts an article title and returns:
        GET populated form if article exists
        POST updated article title and content
    """
    # retrieve form's existing content
    content = util.get_entry(title)
    if not content:
        raise Http404("Page not found")

    # POST edited form to be saved
    if request.method == "POST":
        form = WikipageForm(request.POST)
        if form.is_valid():
            # user inputs
            new_title = form.cleaned_data["title"]
            new_content = form.cleaned_data["content"]

            # file paths
            here = Path(__file__).resolve().parent
            entries_dir = here / "entries"
            old_path = entries_dir / f"{title}.md"
            new_path = entries_dir / f"{new_title}.md"


            # same title 
            if new_title.lower() == title.lower():
                util.save_entry(title, new_content, here)
                return redirect("encyclopedia:get_title", title=title)

            # edited title filname+path == filepath/title of another file
            if new_path.exists():
                messages.error(request, f'An entry titled “{new_title}” already exists.')
                # re-render form so user can pick another title
                return render(request, "encyclopedia/edit.html", {"form": form, "title": title})

            # edited title accepted
            old_path.rename(new_path)   # atomic rename if same filesystem
            util.save_entry(new_title, new_content, here)
            return redirect("encyclopedia:get_title", title=new_title)

        # invalid form  → re-render with errors
        return render(request, "encyclopedia/edit.html", {"form": form, "title": title})
        

    # GET pre-form with existing article
    form = WikipageForm(initial={"title": title, "content": content})

    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "title" : title
    })


def delete(request, title):

    # delete article
    if request.method == "POST":

        # establish rootdir relative to this file
        project_dir = Path(__file__).resolve().parent
        # move filename to static/trash file
        util.move_file_trash(title, project_dir)

        return redirect("encyclopedia:index")

    
    
    return render(request, "encyclopedia/delete.html", {
        "title": title,
    })
    


  


    