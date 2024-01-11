from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET

from .forms import ItemForm
from .models import Item


@require_GET
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)


@require_GET
def item(request: HttpResponse) -> HttpResponse:
    return HttpResponse("This is the item page")


@require_GET
def detail(request: HttpResponse, item_id: int) -> HttpResponse:
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)


@require_http_methods(["GET", "POST"])
def create_item(request: HttpResponse) -> HttpResponse:
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, "food/item-form.html", {'form': form})


@require_http_methods(["GET", "POST"])
def update_item(request: HttpResponse, item_id: int) -> HttpResponse:
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form, 'item' :item})


@require_http_methods(["GET", "POST"])
def delete_item(request: HttpResponse, item_id: int) -> HttpResponse:
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item': item})









