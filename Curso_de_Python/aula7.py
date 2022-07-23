nome = 'Gabriel'
altura = 1.68
idade = 19
peso = 51
e_maior = idade > 18
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é de', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é de {imc:.2f}')
print('{} tem {} anos de idade e seu imc é de {}'.format(nome, idade, imc))
