from django.shortcuts import render

# Create your views here.
# receive a name from user and display a message using http responose and render

def index(request, name):

    return render(request, "hello/greet.html", {
        "greet": name.capitalize()
    })