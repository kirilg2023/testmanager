from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='book_main_en'),
    path('en/', views.index, name='book_main_en'),
    path('ua/', views.index_ua, name='book_main_ua'),
    path('book/', include('book.urls')),
    ]