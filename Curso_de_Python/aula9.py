nome = input('Digite seu nome: ')
altura = input('Digite sua altura: ')
peso = input('Digite seu peso: ')
imc = float(peso) / float(altura) ** 2
print()
print(f'{nome} tem imc de {imc}')
