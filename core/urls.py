from django.urls import path
from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeletaProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/update/', UpdateProdutoView.as_view(), name='upd_produto'),
    path('<int:pk>/del/', DeletaProdutoView.as_view(), name='del_produto'),
]