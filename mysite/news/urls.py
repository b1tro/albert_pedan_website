from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
]