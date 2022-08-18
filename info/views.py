from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def learner(request):
    return render(request, 'learner.html')

def teacher(request):
    return render(request, 'teacher.html')

def informant(reqeust):
    return render(reqeust, 'informant.html')

def home(request):
    return render(request, 'home.html')