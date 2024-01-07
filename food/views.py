from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)


def item(request):
    print(datetime.now() - timedelta(days=7))
    return HttpResponse("This is the item page")