# firstapp/firstapp.py
from django.urls import path
from . import views

urlpatterns = [
    # create path obj refining url pattern to index view
    path(route='', view=views.index, name='index'),
    path(route='date', view=views.get_date, name = 'date')
]