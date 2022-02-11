from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# define all routes
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('architects/', views.ArchitectList.as_view(), name="architect_list"),
    path('architects/new/', views.ArchitectCreate.as_view(), name="architect_create"),
    path('architects/<int:pk>/', views.ArchitectDetail.as_view(), name="architect_detail")
]
