from banco import ContaCorrente, ContaPoupanca, Cliente, Banco

if __name__ == '__main__':
    banco = Banco()

    cliente1 = Cliente("João", 23)
    cliente2 = Cliente("Maria", 39)
    cliente3 = Cliente("Leonardo", 28)
    cliente4 = Cliente("Rafael", 42)

    conta1 = ContaPoupanca(1111, 378372, 0)
    conta2 = ContaCorrente(4444, 904143, 0)
    conta3 = ContaPoupanca(2222, 123403, 0)
    conta4 = ContaCorrente(3333, 894734, 0)

    cliente1.inserir_conta(conta1)
    cliente2.inserir_conta(conta2)
    cliente3.inserir_conta(conta3)
    cliente4.inserir_conta(conta4)

    banco.inserir_cliente(cliente1)
    banco.inserir_conta(conta1)
    banco.inserir_cliente(cliente2)
    banco.inserir_conta(conta2)
    banco.inserir_cliente(cliente3)
    banco.inserir_conta(conta3)
    banco.inserir_cliente(cliente4)
    banco.inserir_conta(conta4)

    if banco.autenticar(cliente1):
        cliente1.conta.depositar(80)
        cliente1.conta.sacar(15)
    else:
        print('Cliente não autenticado. ')

    if banco.autenticar(cliente2):
        cliente2.conta.depositar(15)
        cliente2.conta.sacar(80)
    else:
        print('Cliente não autenticado. ')

    if banco.autenticar(cliente3):
        cliente3.conta.depositar(200)
        cliente3.conta.sacar(10)
    else:
        print('Cliente não autenticado. ')

    if banco.autenticar(cliente4):
        cliente4.conta.depositar(15)
        cliente4.conta.sacar(80)
    else:
        print('Cliente não autenticado. ')




