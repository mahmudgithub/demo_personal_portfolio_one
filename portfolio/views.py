from django.shortcuts import render
from.models import project

def home(request):
    context=project.objects.all()
    return render(request,'portfolio/home.html',{'sos':context})
