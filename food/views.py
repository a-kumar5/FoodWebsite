from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index")


def item(request):
    print(datetime.now() - timedelta(days=7))
    return HttpResponse("This is the item page")