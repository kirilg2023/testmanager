from django.urls import path, re_path
from . import views



urlpatterns = [
    path('<slug:language>/<slug:genre>', views.view_book, name='book_list'),
]