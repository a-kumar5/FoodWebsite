from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.index, name="index"),
    # /food/1/
    path('<int:item_id>/', views.detail, name="detail"),
    # /food/item/
    path('item/', views.item, name="item"),
]
