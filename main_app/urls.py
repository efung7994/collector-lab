from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('crocs/', views.croc_index, name='croc-index'),
  path('crocs/<int:croc_id>/', views.croc_detail, name='croc-detail'),
  path('croc/create/', views.CrocCreate.as_view(), name='croc-create'),
  path('crocs/<int:pk>/update/', views.CrocUpdate.as_view(), name='croc-update'),
  path('crocs/<int:pk>/delete/', views.CrocDelete.as_view(), name='croc-delete'),
  path('crocs/<int:croc_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
  path('crocs/<int:croc_id>/assoc-toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
  path('accounts/signup/', views.signup, name='signup'),
]