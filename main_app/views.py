from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


class Croc:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

crocs = [
  Croc('Lolo', 'tabby', 'Kinda rude.', 3),
  Croc('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Croc('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Croc('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def croc_index(request):
  return render(request, 'crocs/index.html', { 'crocs': crocs })
