carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 1', 20))
carrinho.append(('Produto 1', 50))

# total = [sum(v[1] for v in carrinho)]
total = sum([float(y) for x, y in carrinho])

print(total)
