from django.shortcuts import render, get_object_or_404
from works.models import Works

def works(request):
    tag = request.GET.get('tag')
    contents_works = Works.objects.filter(condition='contents').order_by('-create_date')
    continue_ott_works = Works.objects.filter(condition='continue_ott').order_by('number')
    continue_movie_works = Works.objects.filter(condition='continue_movie').order_by('number')

    if tag == '전체':
        context = {
        'contents_works': contents_works, 
        'continue_ott_works': continue_ott_works,
        'continue_movie_works': continue_movie_works
    }

    elif tag == 'OTT':
        context = {
        'contents_works': contents_works, 
        'continue_ott_works': continue_ott_works,
    }

    elif tag == '영화':
        context = {
        'contents_works': contents_works, 
        'continue_movie_works': continue_movie_works
    }

    else:
        context = {
        'contents_works': contents_works, 
        'continue_ott_works': continue_ott_works,
        'continue_movie_works': continue_movie_works
        }
        
    return render(request, 'works/works.html', context)

def detail(request, works_id):
    index = get_object_or_404(Works, pk=works_id)
    context = {'index': index}
    return render(request,'works/detail.html', context)