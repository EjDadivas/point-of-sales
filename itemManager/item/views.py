from django.shortcuts import render
from django.http.response import HttpResponse
from .models import item 

def item(request):
    return HttpResponse("Hello")

def list_item(request):
    allitems = item.objects.all()
    return render(request, 'item/list_item.html', {'items' : allitems})