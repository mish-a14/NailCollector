from django.shortcuts import render
from .models import Nails

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Hotties ! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def nails_index(request):
  nails = Nails.objects.all()
  return render(request, 'index.html', { 'nails': nails})

def nails_show(request, nail_id):
  nail = Nails.objects.get(id=nail_id)
  return render(request, 'detail.html', { 'nail': nail})
