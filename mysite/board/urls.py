from django.urls import path

from . import views


app_name = 'board'
urlpatterns = [
    path('', views.first.as_view(), name='first'),
]