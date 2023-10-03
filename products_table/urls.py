from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    path('product-list/', login_required(views.ProductListView.as_view()), name='product-list'),
]
