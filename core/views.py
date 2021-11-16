from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoModelForm


class IndexView(ListView):
    model = Produto

    # Template
    template_name = 'index.html'

    # Consulta no banco de dados
    queryset = Produto.objects.all()

    # Recuperar dados do template
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):

    # Ao usar class based view o formulário é criado automaticamente baseado no nosso model
    model = Produto

    template_name = 'produto_form.html'
    fields = ['nome', 'preco']

    # reverse_lazy -> Verifica qual é a view da nossa rota em urls.py e direciona pra ela
    # success_url -> Após preencher o formulário com sucesso, vc será redirecionado pelo reverse_lazy
    success_url = reverse_lazy('index')


class UpdateProdutoView(UpdateView):

    model = Produto

    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class DeletaProdutoView(DeleteView):

    model = Produto

    # Template para confirmar a exclusão do produto
    template_name = 'produto_del.html'

    success_url = reverse_lazy('index')