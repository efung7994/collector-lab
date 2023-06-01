from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Croc, Toy
from .forms import FeedingForm

# Add the following import
from django.http import HttpResponse

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def croc_index(request):
  crocs = Croc.objects.filter(user=request.user)
  return render(request, 'crocs/index.html', { 'crocs': crocs })

@login_required
def croc_detail(request, croc_id):
  croc = Croc.objects.get(id=croc_id)
  toys_croc_doesnt_have = Toy.objects.exclude(id__in = croc.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'crocs/detail.html', { 'croc': croc, 'feeding_form': feeding_form, 'toys': toys_croc_doesnt_have })

class CrocCreate(LoginRequiredMixin, CreateView):
  model = Croc
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/crocs/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CrocUpdate(LoginRequiredMixin, UpdateView):
  model = Croc
  fields = ['breed', 'description', 'age']

class CrocDelete(LoginRequiredMixin, DeleteView):
  model = Croc
  success_url = '/crocs/'

@login_required
def add_feeding(request, croc_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.croc_id = croc_id
    new_feeding.save()
  return redirect('croc-detail', croc_id=croc_id)

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, croc_id, toy_id):
  Croc.objects.get(id=croc_id).toys.add(toy_id)
  return redirect('croc-detail', croc_id=croc_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('croc-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)