from django.shortcuts import render
from django.http import Http404
from . import util



# Create your views here.
def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_title(request, title):

    try:
        html_page = util.get_entry(title)
    except FileNotFoundError:
        raise Http404

    return render(request, "encyclopedia/wikipage.html", {
        "html_page": html_page
    })