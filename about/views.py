from django.shortcuts import render
from django.http import HttpResponse
from works.models import Works

def index(request):
    contents_works = Works.objects.filter(condition='contents').order_by('-create_date')
    continue_ott_works = Works.objects.filter(condition='continue_ott').order_by('number')
    continue_movie_works = Works.objects.filter(condition='continue_movie').order_by('number')

    context = {
        'contents_works' : contents_works,
        'continue_ott_works': continue_ott_works,
        'continue_movie_works': continue_movie_works
    }
    return render(request,'about/index.html', context)

def about(request):
    index = {'studiobeast':'studiobeast'}
    return render(request,'about/about.html', index)