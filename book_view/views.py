from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.

titles = {#словник
    'ukrainian':{
        'Adventures':'Пригоди',
        'The_Horrors':'Жахи',
        'Tragedy':'Трагедія',
        'poetry':'Поезія',
        'language':'мова',


    },
    'english':{
        'apple':'Adventures',
        'banana':'The Horrors',
        'cook':'Tragedy',
        'dima':'poetry',
        'zhongguo':'language',
    },
}

def index(request):
    return render(request, 'book_view/index.html', titles['english'])

def index_ua(request):
    return render(request, 'book_view/index_ua.html', titles['ukrainian'])




