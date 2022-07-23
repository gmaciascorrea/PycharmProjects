# Ex1
def conta(a, b):
    v1 = len(a)
    v2 = len(b)
    print(f'Frase 1: {a}, comprimento: {v1}, Frase 2: {b}, comprimento: {v2}')
    if v1 == v2:
        print(f'Frase 1 e 2 têm o mesmo comprimento: {v1}')
    else:
        print(f'Frase 1 e 2 NÃO têm o mesmo comprimento: {v1}, {v2}')
    if a == b:
        print(f'Frase 1 e 2 têm o mesmo conteúdo. "{a}"')
    else:
        print(f'Frase 1 e 2 NÃO têm o mesmo conteúdo. ')


a = input("Digite uma frase: ")
b = input("Digite outra frase: ")

conta(a, b)


# Ex 2
def mes_nascimento(n):
    if len(n) != 10:
        print("Insira a data no formato solicitado.")
        return
    meses = {0: "Insira um mês válido", 1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
             7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro", }
    if n[3] == '0':
        var = n[4]
    else:
        var = n[3:5]
    for i, j in meses.items():
        if i == int(var):
            return j


n = input("Digite sua data de nascimento(dd/mm/aaaa): ")
data = n[0:2]
print(f"{data} de {mes_nascimento(n)}")


# Ex 3
def informa(l):
    l = str(l)
    var = len(l)
    return var


print(informa(34))


# Ex 4
def calcula(a):
    pass
