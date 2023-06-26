from django.shortcuts import render


def works(request):
    index = {'studiobeast':'studiobeast'}
    return render(request,'works/works.html', index)