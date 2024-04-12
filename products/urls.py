from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.products, name="products"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/like/", views.like, name="like"),
]