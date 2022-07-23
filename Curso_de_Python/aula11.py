num = input('Digite um número inteiro: ')

try:
    num = int(num)
    if num % 2 == 0:
        print('Seu número é par')
    else:
        print('Seu número é ímpar')

except: print('Este não é um número inteiro. Tente novamente.')
