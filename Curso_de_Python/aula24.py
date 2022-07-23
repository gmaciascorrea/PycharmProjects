from itertools import count
import time

contador = count()

for valor in contador:
    print(valor)
    time.sleep(0.5)
###############################################

nums = [-3, 3, 3, 90]


def checar():
    maximo = max(nums)
    minimo = min(nums)
    lista = []

    for i in nums:
        if maximo > i > minimo:
            lista.append(i)

    return len(lista)


print(checar())
