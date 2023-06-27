from django.shortcuts import render, get_object_or_404
from works.models import Works

def works(request):
    index = Works.objects.all().order_by('-create_date')
    context = {'index': index}
    return render(request,'works/works.html', context)

def detail(request, works_id):
    index = get_object_or_404(Works, pk=works_id)
    context = {'index': index}
    return render(request,'works/detail.html', context)