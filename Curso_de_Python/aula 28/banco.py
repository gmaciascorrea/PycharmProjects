from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, quantia):
        self.saldo += quantia
        self.detalhes()
        return

    def detalhes(self):
        print(f'Agência: {self.agencia} Conta: {self.conta} Saldo {self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, quantia):
        if (self.saldo + self.limite) < quantia:
            print('Saldo insuficiente')
            return

        self.saldo -= quantia
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, quantia):
        if self.saldo < quantia:
            print('Saldo insuficiente')
            return

        self.saldo -= quantia
        self.detalhes()


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            print("A conta é inválida.", end=" ")
            return False

        if cliente.conta.agencia not in self.agencias:
            print("A agência é inválida.", end=" ")
            return False

        return True
