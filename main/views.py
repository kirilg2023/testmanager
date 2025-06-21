from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import random
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    a = random.randint(1, 100)
    return render(request, 'main/about.html', {'random':a})

def about_ua(request):
    b = random.randint(1, 100)
    return render(request, 'main/test.html', {'random':b})

def index_ua(request):
    return render(request, 'main/ukraine.html')

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Сторінка не знайдена</h1>")
