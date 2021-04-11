from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about),
    path('index/', views.nails_index),
    path('index/<int:nail_id>/', views.nails_show, name='detail'),
]


