from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoModelForm


class IndexView(ListView):
    models = Produto

    # Template
    template_name = 'index.html'

    # Consulta no banco de dados
    queryset = Produto.objects.all()

    # Recuperar dados do template
    context_object_name = 'produtos'

