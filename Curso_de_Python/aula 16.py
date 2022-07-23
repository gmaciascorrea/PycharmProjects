cpf = input('Digite um cpf: ')
soma = 0
cpf = cpf.split('.')
novo_cpf = ''

for elem in cpf:
    novo_cpf += elem

novo_cpf = novo_cpf.split('-')

novo2 = ''
for elem in novo_cpf:
    novo2 += elem

print(cpf, novo_cpf, novo2)

novo3 = novo2[:9]

reverso = 10
for index in range(19):
    if index > 8:
        index -= 9

    print(index, reverso)

    reverso -= 1
    if reverso < 2:
        reverso = 11




