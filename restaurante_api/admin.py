from django.contrib import admin
from .models import (
    Fornecedor, Ingrediente, Compra, Categoria, Produto,
    ProdutoIngrediente, Funcionario, Mesa, Cliente,
    Pedido, Pagamento, ItemPedido
)


admin.site.register(Fornecedor)
admin.site.register(Ingrediente)
admin.site.register(Compra)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(ProdutoIngrediente)
admin.site.register(Funcionario)
admin.site.register(Mesa)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Pagamento)
admin.site.register(ItemPedido)
