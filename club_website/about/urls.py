from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.about_page, name='about_page'),
]