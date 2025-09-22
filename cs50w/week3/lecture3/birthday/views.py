from django.shortcuts import render
from datetime import datetime


def birthday(request, name):

    people = {
        "daniel": datetime(1978, 9, 4),
        "banda": datetime(2009, 8, 18),
    }
    today = datetime.now()
    birthday = people[name]

    return render(request, "birthday/message.html", {
        "birthday": today.month == birthday.month and today.day == birthday.day,
        "name": name.capitalize()

    })