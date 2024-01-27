from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    # /food/
    # path('', views.index, name="index"),
    path('', views.IndexClassView.as_view(), name="index"),
    # /food/1/
    #path('<int:item_id>/', views.detail, name="detail"),
    path('<int:pk>/', views.FoodDetails.as_view(), name="detail"),
    # /food/item/
    path('item/', views.item, name="item"),
    # path('add/', views.create_item, name="create_item"),
    path('add/', views.FoodCreateItem.as_view(), name='create_item'),
    #path('update/<int:item_id>/', views.update_item, name="update_item"),
    path('update/<int:pk>/', views.FoodUpdateItem.as_view(), name="update_item"),
    #path('delete/<int:item_id>', views.delete_item, name="delete_item")
    path('delete/<int:pk>', views.FoodDeleteItem.as_view(), name="delete_item")
]
