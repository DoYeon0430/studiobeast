from django.shortcuts import render, get_object_or_404
from .models import News

def news(request):
    index = News.objects.all().order_by('-create_date')
    context = {'index': index}
    return render(request,'news/news.html', context)

def detail(request, news_id):
    index = get_object_or_404(News, pk=news_id)
    context = {'index': index}
    return render(request,'news/detail.html', context)