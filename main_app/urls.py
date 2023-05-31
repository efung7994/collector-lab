from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('crocs/', views.croc_index, name='croc-index'),
  path('crocs/<int:croc_id>/', views.croc_detail, name='croc-detail'),
  path('croc/create/', views.CrocCreate.as_view(), name='croc-create'),
  path('crocs/<int:pk>/update/', views.CrocUpdate.as_view(), name='croc-update'),
  path('crocs/<int:pk>/delete/', views.CrocDelete.as_view(), name='croc-delete'),
]