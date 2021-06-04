from django.conf.urls import url
from django.urls.conf import path
from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
]