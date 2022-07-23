l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [1, 2, 3, 4, 5, 6]
l3 = zip(l1, l2)
l4 = []

for key, value in l3:
    l4.append(key + value)

print(l4)

lista_soma = [x + y for x, y in zip(l1, l2)]

print(lista_soma)
