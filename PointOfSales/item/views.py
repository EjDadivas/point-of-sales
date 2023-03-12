from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import item


def item_view(request):
    return redirect('list_item')


def list_item(request):
    allitems = item.objects.all()
    return render(request, 'item/list_item.html', {'items': allitems})


def add_item(request):
    if (request.method == "POST"):
        itname = request.POST.get("itname")
        itprice = request.POST.get("itprice")
        item.objects.create(item_name=itname, item_price=itprice)
    return redirect('list_item')


def delete_item(request, pk):
    item.objects.filter(pk=pk).delete()
    return redirect('list_item')


def update_item(request, pk):
    it = item.objects.get(pk=pk)
    if request.method == "POST":
        itname = request.POST.get("itname")
        itprice = request.POST.get("itprice")
        it.item_name = itname
        it.item_price = itprice
        it.save()
        return redirect('list_item')
    return render(request, 'item/update_item.html', {'item': it})
