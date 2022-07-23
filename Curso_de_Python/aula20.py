lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [4, 5, 3, 7, 2, 5, 1, 8, 8, 2],
    [4, 6, 7, 4, 2, 7, 8, 6, 9, 2],
    [3, 7, 8, 4, 1, 7, 9, 4, 2, 10],
    [9, 7, 5, 7, 3, 2, 10, 9, 6, 7],
    [4, 2, 6, 7, 10, 8, 7, 9, 3, 10],
    [9, 6, 2, 5, 3, 9, 8, 1, 1, 8],
    [10, 4, 1, 3, 5, 8, 5, 1, 9, 10],
    [3, 5, 10, 9, 8, 3, 9, 8, 6, 4]
]


def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))
