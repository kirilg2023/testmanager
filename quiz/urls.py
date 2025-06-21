from django.urls import path
from . import views


urlpatterns=[
    path('view/<slug:main>', views.main, name='cheese_main'),
    path('game/<slug:q>', views.game, name='cheese_game'),


]