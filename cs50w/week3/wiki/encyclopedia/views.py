from django.shortcuts import render
from . import util
from http import r



# Create your views here.
def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):

    article_markdown = util.get_entry(title)
    article_html = article_markdown.markdown()

