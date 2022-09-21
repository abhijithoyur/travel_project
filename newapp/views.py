from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Persons
def fun1(request):
    obj=Place.objects.all()
    obj1=Persons.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

