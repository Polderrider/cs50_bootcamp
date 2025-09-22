from django.shortcuts import render
import datetime

# Create your views here.
# returns yes if the date is january 1st, otherwise returns no
def celebrate(request):

    now = datetime.datetime.now()
    
    return render(request, "newyear/check.html", {
        "answer": now.day == 1 and now.month == 1
    })