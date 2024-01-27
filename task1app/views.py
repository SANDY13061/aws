from django.shortcuts import render
from task1app.models import student

# Create your views here.
def index(request):
    res=student.objects.all()
    return render(request,'index.html',{'res':res})
def python(request):
    res=student.objects.all()
    return render(request,'python.html',{'res':res}) 
def java(request):
    res=student.objects.all()
    return render(request,'java.html',{'res':res}) 