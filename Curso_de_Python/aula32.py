a = int(input())
for i in range(1, 11):
    print(f'{a} x {i} = {a*i}')

vezes = int(input())
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
for i in range(vezes):
    print(alfabeto[i]*(i+1))

div = int(input())
parcela = int(input())
pagamento = 0
while True:
    pagamento += 1
    if div / parcela >= 1:
        print(f'pagamento: {pagamento}')
        print(f'antes = {div}')
        print(f'depois = {div - parcela}')
        div -= parcela
        print('-----')
    elif div / parcela > 0:
        print(f'pagamento: {pagamento}')
        print(f'antes = {div}')
        print(f'depois = 0')
        print('-----')
        break
    else:
        break

bi = 0
inicio = int(input())
fim = int(input())

while inicio <= fim:
    if (inicio % 4 == 0 and inicio % 100 != 0) or (inicio % 400 == 0):
        print(inicio)
        bi += 1
        inicio += 1
    else:
        inicio += 1
print('bissextos:', bi)

inicio = int(input())
fim = int(input())
primo = 0
if inicio <= fim <= 5000:
    for i in range(inicio, fim+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)
                primo += 1
print('primos:', primo)
