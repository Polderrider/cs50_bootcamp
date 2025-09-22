from django.shortcuts import render
import datetime
# Create your views here.
def dinnertime(request):

    now = datetime.datetime.now()
    
    return render(request, "dinnertime/message.html", {
        "dinnertime": now.hour > 7
    })