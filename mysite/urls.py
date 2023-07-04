"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.views.static import serve
from django.views.generic import TemplateView

urlpatterns = [
    path("", include("about.urls")),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    path("about/", include("about.urls")),
    path("works/", include("works.urls")),
    path("news/", include("news.urls")),
    path("contact/", include("contact.urls")),

    #Admin
    path('admin/', admin.site.urls),

    #TINYMCE
    path('tinymce/', include('tinymce.urls')),

    #robots.txt
    path('robots.txt',  TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),

    #sitemap.xml
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)