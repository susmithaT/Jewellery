

from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.ItemSaveorUpdate, name="item"),
    path('material/', views.MaterialSaveorUpdate, name="material"),
    path('order/', views.OrderSaveorUpdate, name="order"),
    path('searchitem/', views.searchItem, name="searchitem"),
    path('searchmaterial/', views.searchMaterial, name="searchmaterial"),
    path('searchorder/', views.searchOrder, name="searchorder"),

]
