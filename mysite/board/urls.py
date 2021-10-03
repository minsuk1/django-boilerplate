from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


app_name = 'board'
urlpatterns = [
    path('', csrf_exempt(views.first.as_view()), name='first'),
    path('', csrf_exempt(views.redis.as_view()), name='redis'),
]