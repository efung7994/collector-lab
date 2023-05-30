from django.shortcuts import render
from .models import Croc

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def croc_index(request):
  crocs = Croc.objects.all()
  return render(request, 'crocs/index.html', { 'crocs': crocs })

def croc_detail(request, croc_id):
  croc = Croc.objects.get(id=croc_id)
  return render(request, 'crocs/detail.html', { 'croc': croc })
