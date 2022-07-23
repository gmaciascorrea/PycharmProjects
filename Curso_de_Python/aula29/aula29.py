import re


class CalcIpv4:
    def __init__(self, ip=None, mascara=None, cidr=None):
        self._ip = ip
        self._mascara = mascara
        self._cidr = cidr
        self._broadcast = None
        self._rede = None
        self._numero_ips = None

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def cidr(self):
        return self._cidr

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def rede(self):
        return self._rede

    @property
    def numero_ips(self):
        return self._numero_ips

    def calcula_broadcast(self):
        if self.ip is None:
            print('Por favor insira um IP válido.')
            return
        if self.mascara and self.cidr is None:
            print('Por favor insira máscara ou CIDR do IP.')
            return
        pass

    def fatia(self):
        var = re.sub(r'[^0-9]', '', self.ip)
        var1 = int(var[0:3])
        bin1 = binario(self, var1)
        var2 = int(var[3:6])
        var3 = int(var[6])
        var4 = int(var[7:9])
        # print(var1, '', var2, '', var3, '', var4)

    def binario(self, num):
        binario = ''
        if num - 128 >= 0:
            num -= 128
            binario += '1'
        else:
            binario += '0'
        if num - 64 >= 0:
            num -= 64
            binario += '1'
        else:
            binario += '0'
        if num - 32 >= 0:
            num -= 32
            binario += '1'
        else:
            binario += '0'
        if num - 16 >= 0:
            num -= 16
            binario += '1'
        else:
            binario += '0'
        if num - 8 >= 0:
            num -= 8
            binario += '1'
        else:
            binario += '0'
        if num - 4 >= 0:
            num -= 4
            binario += '1'
        else:
            binario += '0'
        if num - 2 >= 0:
            num -= 2
            binario += '1'
        else:
            binario += '0'
        if num - 1 >= 0:
            num -= 2
            binario += '1'
        else:
            binario += '0'


if __name__ == '__main__':
    calc_ipv4 = CalcIpv4(ip='192.168.0.25', mascara='255.255.255.192')
    print(f'IP: {calc_ipv4.ip}')
    print(f'Máscara: {calc_ipv4.mascara}')
    print(f'Rede: {calc_ipv4.rede}')
    print(f'Broadcast: {calc_ipv4.broadcast}')
    print(f'Prefixo: {calc_ipv4.cidr}')
    print(f'Número de IPs da rede: {calc_ipv4.numero_ips}')
