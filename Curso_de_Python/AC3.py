# def converte_inteiro(lista):
#     for i in range(len(lista)):
#         lista[i] = int(lista[i])
#
#
# def exibe(carrinho):
#     for i in range(len(carrinho)):
#         if i < len(carrinho) -1:
#             print(carrinho[i], end=' ')
#         else:
#             print(carrinho[i])
#
#
# carrinho = input().split()
# if carrinho != []:
#     converte_inteiro(carrinho)
# comando = input().split()
# while comando[0] != 'encerrar':
#     if comando[0] == 'adicionar':
#         carrinho.append(int(comando[1]))
#     elif comando[0] == 'remover':
#         comando[1] = int(comando[1])
#         if comando[1] in carrinho:
#             carrinho.remove(comando[1])
#         else:
#             print(f'código {comando[1]} não encontrado')
#     else:
#         carrinho.sort()
#         exibe(carrinho)
#     comando = input().split()
# carrinho.sort()
# exibe(carrinho)


# A = int(input())
# B = int(input())
#
# if A > B:
#     print('Nenhuma tabuada no intervalo!')
# else:
#     for num in range(A, B+1):
#         for numero in range(1, 11):
#             print(f'{num} x {numero} = {num * numero}')
#         print('-'*10)


# def coleta_canais(qtd_canais):
#     canais = []
#     for _ in range(qtd_canais):
#         nome, inscritos, monetizacao, premium = input().split(';')
#         inscritos = int(inscritos)
#         monetizacao = float(monetizacao)
#         premium = premium == 'sim'
#         canais.append([nome, inscritos, monetizacao, premium])
#     return canais
#
#
# def bonificacao(canais, fixo_premium, fixo_nao_premium):
#     bonus = []
#     for canal in canais :
#         valor = canal[2]
#         if canal[3]:
#             valor += canal[1] // 1000 * fixo_premium
#         else:
#             valor += canal[1] // 1000 * fixo_nao_premium
#         bonus.append([canal[0], valor])
#     return bonus
#
#
# def exibe(bonus):
#     print(5*'-')
#     print('BÔNUS')
#     print(5*'-')
#     for registro in bonus:
#         print(f'{registro[0]}: R$ {registro[1]:.2f}')
#
#
# qtd_canais = int(input())
# canais = coleta_canais(qtd_canais)
# fixo_premium = float(input())
# fixo_nao_premium = float(input())
# bonus = bonificacao(canais, fixo_premium, fixo_nao_premium)
# exibe(bonus)


# tempo = int(input())
# tempos = []
# while not tempo < 0:
#     tempos.append(tempo)
#     tempo = int(input())
#
# acumula = 0
# for i in tempos:
#     acumula += i
#
# media = acumula / len(tempos)
# print(f'MEDIA: {media:.2f}')
# for i in tempos:
#     if i < media:
#         print(i)


qtd_alunos = int(input())
originais = []
segunda_chance = []
notas_finais = []

for i in range(qtd_alunos*2):
    if i < qtd_alunos:
        nota = float(input())
        originais.append(nota)
    else:
        nota = float(input())
        segunda_chance.append(nota)
calculo = originais.copy()
notas_alteradas = 0

indice = 0
for i in range(qtd_alunos):
    if calculo[indice] == 10.0:
        notas_finais.append(calculo[indice])
        indice += 1
    else:
        if segunda_chance[indice] == 10.0:
            if (calculo[indice] + 2) > 10.0:
                notas_finais.append(10.0)
                notas_alteradas += 1
            else:
                calculo[indice] += 2
                notas_finais.append(calculo[indice])
                notas_alteradas += 1
        else:
            notas_finais.append(calculo[indice])
        indice += 1

print(f'NOTAS ALTERADAS: {notas_alteradas}')
for i in range(qtd_alunos):
    if originais[i] == notas_finais[i]:
        print(f'-(00{i + 1}) original: {originais[i]:05.2f} | final: {notas_finais[i]:05.2f}')
    else:
        print(f'*(00{i + 1}) original: {originais[i]:05.2f} | final: {notas_finais[i]:05.2f}')

