from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    prority = forms.IntegerField(label="Priority", max_value=10, min_value=1)


# tasks = ['foo', 'bar', 'baz']
tasks = []


def index(request):

    if "tasks" not in request.session:
        request.session["tasks"] = []


    return render(request, "tasks/tasklist.html", {
        "tasks": request.session["tasks"]
})


def add(request):
     
    # check POST -> 
    #          new instance of form passing request.POST data as a parameter ->
                # .clean form data extrating task str from form dict and save in variable
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        # form valid
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))

        # form not valid, return the same form with data
        else:
            return render(request, "tasks/add.html", {
                "forms": form
            })


    # GET method renders a new empty form
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })



