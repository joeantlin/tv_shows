from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show
import datetime

def index(request):
    context = {
        "allshows": Show.objects.all().values()
    }
    #print(context)
    return render(request, "watch/index.html", context)

def showpage(request, showid):
    context = {
        "theshow": Show.objects.get(id=showid)
    }
    return render(request, "watch/read.html", context)

#Show editor
def editpage(request, editid):
    context = {
        "editshow": Show.objects.get(id=editid)
    }
    return render(request, "watch/edit.html", context)

#Show edits
def editedshow(request):
    if request.method == "POST":
        idshow = request.POST["showid"]
        thisshow = Show.objects.get(id=idshow)

        errors = Show.objects.edit_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/"+idshow+"/edit")
        else:
            ti = request.POST["title"]
            ne = request.POST["network"]
            de = request.POST["description"]
            da = request.POST["date"]
            thisshow.title = ti
            thisshow.network = ne
            thisshow.desc = de
            if not len(da) < 10:
                thisshow.release = da
            thisshow.save()
            return redirect("/shows/"+idshow)

#Show creator
def createpage(request):
    return render(request, "watch/new.html")

#New show
def newshow(request):
    if request.method == "POST":
        errors = Show.objects.add_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/create")
        else:
            ti = request.POST["title"]
            ne = request.POST["network"]
            da = request.POST["date"]
            de = request.POST["description"]
            Show.objects.create(title=ti, network=ne, release=da, desc=de)
            return redirect("/shows")

def deleteshow(request, deleteid):
    Show.objects.get(id=deleteid).delete()
    return redirect("/shows")