from django.shortcuts import render, get_object_or_404
from .models import News
from django.core.paginator import Paginator

def news(request):
    news_list = News.objects.all().order_by('-create_date')
    paginator = Paginator(news_list, 5)  # 한 페이지에 보여줄 게시글 수를 5로 설정
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'news/news.html', context)

def detail(request, news_id):
    index = get_object_or_404(News, pk=news_id)
    context = {'index': index}
    return render(request,'news/detail.html', context)