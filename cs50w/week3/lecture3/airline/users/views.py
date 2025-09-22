from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# import needed for login/logout views below
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    return render(request, "users/user.html")


def login_view(request):

    if request.method == "POST":
        # allocate vars to username and password
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate user
        user = authenticate(request, username=username, password=password)

        # user == None means auth was unsuccssful
        if user is not None:  # not none mean succesful auth
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else: # login unsuccessful
            return render(request, "users/login.html", {
                "message": "Invalid login credentials",
            })


    # GET method - show empty form
    return render(request, "users/login.html")    


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))