from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('crocs/', views.croc_index, name='croc-index'),
  path('crocs/<int:croc_id>/', views.croc_detail, name='croc-detail'),
]