# /firstapp views.py
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today is {}"\
                "</html>".format(today)
    return HttpResponse(content=template)

def index(request):
    # Create a simple html page as a string
    template = "<html>" \
                "This is your first view" \
               "</html>"
    # Return the template as content argument in HTTP response
    return HttpResponse(content=template)