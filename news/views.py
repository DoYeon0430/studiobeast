from django.shortcuts import render


def news(request):
    index = {'studiobeast':'studiobeast'}
    return render(request,'news/news.html', index)