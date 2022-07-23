palavraSecreta = 'gabriel'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu')
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print('Você digitou mais que uma letra. Tente novamente')
        continue

    digitadas.append(letra)

    if letra in palavraSecreta:
        print(f'Uhull, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'Que pena, a letra "{letra}" não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in palavraSecreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '-'

    if secreto_temporario == palavraSecreta:
        print(f"Parabéns, você ganhou. A palavra era '{palavraSecreta}'")
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in palavraSecreta:
        chances -= 1
    print(f'Você ainda tem {chances} chances')
    print()
