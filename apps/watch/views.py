from django.shortcuts import render, HttpResponse, redirect
from .models import Show

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

        ti = request.POST["title"]
        thisshow.title = f"{ti}"

        ne = request.POST["network"]
        thisshow.network = f"{ne}"

        da = request.POST["date"]
        thisshow.release = f"{da}"

        de = request.POST["description"]
        thisshow.desc = f"{de}"

        thisshow.save()
        return redirect("/shows/"+idshow)

#Show creator
def createpage(request):
    return render(request, "watch/new.html")

#New show
def newshow(request):
    if request.method == "POST":
        ti = request.POST["title"]
        ne = request.POST["network"]
        da = request.POST["date"]
        de = request.POST["description"]
        Show.objects.create(title=f"{ti}", network=f"{ne}", release=f"{da}", desc=f"{de}")
        return redirect("/shows")

def deleteshow(request, deleteid):
    Show.objects.get(id=deleteid).delete()
    return redirect("/shows")