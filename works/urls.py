from django.urls import path

from . import views

app_name = 'works'

urlpatterns = [
    path("", views.works, name="works"),
]