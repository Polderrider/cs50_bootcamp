from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from . import util



# Create your views here.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_title(request, title):
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




    


    