from django.shortcuts import render


def contact(request):
    index = {'studiobeast':'studiobeast'}
    return render(request,'contact/contact.html', index)