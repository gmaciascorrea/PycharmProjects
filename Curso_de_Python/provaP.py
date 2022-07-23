z1 = 0
r1 = input("Qual a sentença?")

r1 = r1.split()
r2 = r1[0]
r3 = r2[0]


for x in r1:
    if x[0] == r3:
        z1 = z1 + 1
        if z1 == len(r1):
            print('Y')
    else:
        print('N')
        break


def seila():
    frase = input("Qual a sentença?")

    lista_de_palavras = frase.split()
    primeira_letra = (frase[0])[0]

    for palavra in lista_de_palavras:
        if palavra[0] != primeira_letra:
            return False
    return True


if seila():
    print("yes")
else:
    print("no")

# oi tudo ok onde outros ogros oram?

