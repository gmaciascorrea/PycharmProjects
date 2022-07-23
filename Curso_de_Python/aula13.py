nome = input('Digite seu primeiro nome: ')
nome = len(nome)

if nome <= 4:
    print('Seu nome é curto.')
elif nome > 4 and nome <= 6 :
    print('Seu nome é normal.')
elif nome > 6 :
    print('Seu nome é muito grande.')
else: print()
