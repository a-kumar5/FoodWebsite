from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from .forms import ItemForm
from .models import Item


@require_GET
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


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


class FoodDetails(DetailView):
    model = Item
    template_name = 'food/detail.html'


@require_http_methods(["GET", "POST"]) # Sensitive
def create_item(request: HttpResponse) -> HttpResponse:
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, "food/item-form.html", {'form': form})


class FoodCreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)



@require_http_methods(["GET", "POST"]) # Sensitive
def update_item(request: HttpResponse, item_id: int) -> HttpResponse:
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form, 'item' :item})


class FoodUpdateItem(UpdateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')


@require_http_methods(["GET", "POST"]) # Sensitive
def delete_item(request: HttpResponse, item_id: int) -> HttpResponse:
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item': item})


class FoodDeleteItem(DeleteView):
    model = Item
    success_url = reverse_lazy("food:index")
    template_name = "food/item-delete.html"






