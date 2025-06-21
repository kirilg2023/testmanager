from django.urls import path
from . import views
from .views import page_not_found


urlpatterns=[
    path('', views.index, name='home'),
    path('about',views.about, name='about'),
    path('test',views.about_ua, name='test'),
    path('test1',views.index_ua, name='test1')

]
handler404= page_not_found
