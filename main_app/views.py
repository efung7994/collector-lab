from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Croc
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'crocs/detail.html', { 'croc': croc, 'feeding_form': feeding_form })

class CrocCreate(CreateView):
  model = Croc
  fields = '__all__'
  success_url = '/crocs/'

class CrocUpdate(UpdateView):
  model = Croc
  fields = ['breed', 'description', 'age']

class CrocDelete(DeleteView):
  model = Croc
  success_url = '/crocs/'

def add_feeding(request, croc_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.croc_id = croc_id
    new_feeding.save()
  return redirect('croc-detail', croc_id=croc_id)
