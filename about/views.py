from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    index = {'studiobeast':'studiobeast'}
    return render(request,'about/index.html', index)

def about(request):
    index = {'studiobeast':'studiobeast'}
    return render(request,'about/about.html', index)