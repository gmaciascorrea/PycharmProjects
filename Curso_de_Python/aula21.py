string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
l1 = [(i, i + n) for i in range(0, len(string), n)]
lista = [string[i:i + n] for i in range(0, len(string), n)]
retorno = ".".join(lista)

print(string)
print(l1)
print(lista)
print(retorno)
