from django.shortcuts import render
from portfolio.models import Project
# Create your views here.


def models(request):
    models=Project.objects.all()
    return render(request,"model.html",{"models":models})

def modeldetail(request,slug):
    model=Project.objects.get(slug=slug)
    modelpost=model.projectimage_set.all()
    return render(request,"modeldetail.html",{"model":model,"posts":modelpost})