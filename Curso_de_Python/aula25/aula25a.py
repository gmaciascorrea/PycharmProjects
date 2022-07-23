from aula25b import valida

cnpj = '04.252.011/0001-10'
# cnpj = '11.111.111/1111-11'

if __name__ == '__main__':
    if valida(cnpj):
        print('O CNPJ inserido é válido')
    else:
        print('O CNPJ inserido NÃO é válido')
