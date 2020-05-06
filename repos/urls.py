from django.urls import path

from . import views

appname = 'repos'
urlpatterns = [
    path('', views.index, name='index'),
]
