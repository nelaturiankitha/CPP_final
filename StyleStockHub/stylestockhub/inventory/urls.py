from django.urls import include, path
from .views import add_product, delete, inventory_list, per_product_view,update

urlpatterns = [
    path("",inventory_list, name="inventory_list"),
    path("per_product/<int:pk>",per_product_view, name="per_product"),
    path("add/", add_product, name="product_add"),
    path("delete/<int:pk>/", delete, name="product_delete"),
    path("product_update/<int:pk>/", update, name="product_update"),
]