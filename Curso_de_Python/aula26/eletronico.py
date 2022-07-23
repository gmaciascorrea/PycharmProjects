from log import LogMixin


class Eletronico(LogMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            info = f'{self._nome} já está ligado.'
            print(info)
            self.log_error(info)
            return
        self._ligado = True
        info = f'{self._nome} foi ligado com sucesso.'
        print(info)
        self.log_error(info)
        return

    def desligar(self):
        if not self._ligado:
            info = f'{self._nome} já está desligado.'
            print(info)
            self.log_error(info)
            return
        self._ligado = False
        info = f'{self._nome} foi desligado.'
        print(info)
        self.log_error(info)
        return
