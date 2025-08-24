from django.shortcuts import render
from . import util



# Create your views here.
def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_title(request, title):

    html_page = util.get_entry(title)

    return render(request, "encyclopedia/wikipage.html", {
        "html_page": html_page
    })