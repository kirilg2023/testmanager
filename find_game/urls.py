from django.urls import path
from. import views


urlpatterns=[
    path('', views.game_home, name='news_home'),
    path('<slug:post_slug>/', views.game_detail, name='news-detail'),

]