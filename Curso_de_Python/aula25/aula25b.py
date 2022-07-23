import re


def valida(cnpj):
    print(f"Número a ser validado: {cnpj}")
    cnpj_limpo = limpa(cnpj)

    if eh_seguencia(cnpj_limpo):
        return False

    cnpj_primeiro = cnpj_limpo + str(digito(checa_primeiro(cnpj_limpo)))
    final = formata(cnpj_primeiro + str(digito(checa_primeiro(cnpj_primeiro, n=6))))

    print()
    print(f"Número obtido pela validação: {final}")

    if cnpj == final:
        return True
    else:
        return False


def limpa(cnpj):
    var = re.sub(r'[^0-9]', '', cnpj)
    var = var[:-2]
    return var


def checa_primeiro(cnpj, n=5):
    acumula = 0
    for i in cnpj:
        acumula += n * int(i)
        if n == 2:
            n = 10
        n -= 1
    # print(f"Soma é equivalente a {acumula}")
    return acumula


def digito(num):
    var = 11 - (num % 11)
    if var > 9:
        var = 0
    return var


def eh_seguencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def formata(cnpj):
    return "%s.%s.%s/%s-%s" % (cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14])
