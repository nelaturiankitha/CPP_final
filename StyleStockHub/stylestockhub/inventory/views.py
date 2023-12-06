from django.shortcuts import get_object_or_404, redirect, render
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import InventoryUpdateForm, AddInventoryForm
from django.contrib import messages

# def index(request):
#     context = {
#         "title":"Index"
#     }
#     return render(request, "inventory/index.html", context=context)

@login_required()
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        "title" : "Inventory List",
        "inventories" : inventories
    }
    return render(request, "inventory/inventory_list.html", context=context)

@login_required()
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory
    }
    return render(request, "inventory/per_product.html", context=context)


@login_required()
def add_product(request):
    if request.method == "POST":
        updateForm = AddInventoryForm(data=request.POST)
        if updateForm.is_valid():
            new_invetory = updateForm.save(commit=False)
            new_invetory.sales = float(updateForm.data['cost_per_item']) * float(updateForm.data['quantity_sold'])
            new_invetory.save()
            messages.success(request, "Successfully Added Product")
            return redirect(f"/inventory/")
    else:
        updateForm = AddInventoryForm()

    return render(request, "inventory/inventory_add.html", {'form' : updateForm})


@login_required()
def delete(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    messages.success(request, "Inventory Deleted")
    return redirect("/inventory/")

@login_required()
def update(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = InventoryUpdateForm(data=request.POST)
        if updateForm.is_valid():
            inventory.name = updateForm.data['name']
            inventory.quantity_in_stock = updateForm.data['quantity_in_stock']
            inventory.quantity_sold = updateForm.data['quantity_sold']
            inventory.cost_per_item = updateForm.data['cost_per_item']
            inventory.sales = float(inventory.cost_per_item) * float(inventory.quantity_sold)
            inventory.save()
            messages.success(request, "Update Successful")
            return redirect(f"/inventory/")
    else:
        updateForm = InventoryUpdateForm(instance=inventory)

    return render(request, "inventory/inventory_update.html", {'form' : updateForm})


