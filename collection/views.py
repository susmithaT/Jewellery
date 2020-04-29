from django.shortcuts import render, redirect
from .forms import ItemForm, OrderForm, MaterialForm
from django.contrib import messages
from .models import Item, Material, Order
from .filters import ItemFilter
from django.db.models import Q


# Create your views here.
def ItemSaveorUpdate(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Item added succesfully")
            return redirect('item')
    elif request.method == 'PUT':
        item = Item.objects.get(pk=id)
        form = ItemForm(instance=item)
        form.save()
    else:
        # item = Item.objects.get(pk=id)
        form = ItemForm()
    return render(request, 'addItem.html', {"form": form, 'itemobjects': Item.objects.all})


def MaterialSaveorUpdate(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            # itemobjects = Item.objects.all()
            messages.add_message(request, messages.SUCCESS, "Material added succesfully")
            return redirect('material')
    elif request.method == 'PUT':
        item = Material.objects.get(pk=id)
        form = MaterialForm(instance=item)
        form.save()
    else:
        # item = Item.objects.get(pk=id)
        form = MaterialForm()
    return render(request, 'addMaterial.html', {"form": form, 'MaterialObjects': Material.objects.all})


def OrderSaveorUpdate(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Order added succesfully")
            return redirect('order')
    elif request.method == 'PUT':
        item = Item.objects.get(pk=id)
        form = OrderForm(instance=item)
        form.save()
    else:
        # item = Item.objects.get(pk=id)
        form = OrderForm()
    return render(request, 'addOrder.html', {"form": form,'orderobjects':Order.objects.all})


def searchItem(request):
    itemobjects = Item.objects.filter(name__contains=request.POST['searchstring'])
    form = ItemForm()
    return render(request, 'addItem.html', {"form": form, 'itemobjects': itemobjects})


def searchMaterial(request):
    materialobjects = Material.objects.filter(metal__contains=request.POST['searchstring'])
    form = MaterialForm()
    return render(request, 'addMaterial.html', {"form": form, 'MaterialObjects': materialobjects})

def searchOrder(request):
    searchobj = request.POST['searchstring']
    form = OrderForm()
    if searchobj is None:
        orderobjects=None
    else:
        itemobj = Item.objects.filter(name__contains=searchobj).values('name')
        orderobjects = Order.objects.filter(item__in =itemobj).distinct
        #Item.objects.filter(Q(creator=owner) | Q(moderated=False))

        orderobjects = Order.objects.filter(Q(item__in=itemobj) | Q(customername__contains=searchobj)).distinct
    return render(request, 'addOrder.html', {"form": form, 'orderobjects': orderobjects})