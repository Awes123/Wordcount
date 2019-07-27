from django.urls import path
from .import views
urlpatterns = [
path('', views.homepage,name='home'),
path('Count/',views.Count,name='Count'),
path('About/',views.About,name='About'),
]
