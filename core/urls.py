from django.urls import path
from .views import IndexView, CreateProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateProdutoView.as_view(), name='add_produto'),
]