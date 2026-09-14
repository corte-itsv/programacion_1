class CuentaBancaria:
    contador = 0

    def __init__(self, titular, saldo):
        CuentaBancaria.contador += 1
        self.id = CuentaBancaria.contador
        self.titular = titular
        self.saldo = saldo
    
    def __str__(self):
        return f"id = {self.id}, titular: {self.titular}, monto: {self.saldo}"

    def __repr__(self):
        return f"CuentaBancaria(id = {self.id},{self.titular},{self.saldo})"

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        else:
            return False

    def consultar_saldo(self):
        return self.saldo

    def retirar(self, monto):
        if monto > 0 and self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False

    def transferir(self, monto, destino):
        if self.retirar(monto) == True:
            destino.depositar(monto)
            return True
        else:
            return False

class CuentaAhorro(CuentaBancaria):

    def __init__(self,titular,saldo,interes):
        super().__init__(titular,saldo)
        self.interes = interes

    def aplicar_interes(self):
        interes_aplicado = self.saldo * self.interes
        self.depositar(interes_aplicado)


class CuentaCorriente(CuentaBancaria):

    def __init__(self,titular,saldo,credito):
        super().__init__(titular,saldo)
        self.credito = credito

    def retirar(self, monto):
        if monto > 0 and self.saldo + self.credito >= monto:
            self.saldo -= monto
            return True
        else:
            return False











#cuenta1 = {'titular': 'Cortesini Luciano', 'saldo': 0}
#cuenta2 = {'titular': 'Cortesini Luciano', 'saldo': 0}
#
#def depositar(cuenta, monto):
#    cuenta['saldo'] += monto
#
#depositar(cuenta1,10)


