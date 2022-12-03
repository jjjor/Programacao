class Conta():

    def __init__(self, numero, nome, saldo, limite):
        
        self._numero = numero
        self._nome = nome
        self._saldo = saldo
        self._limite = limite

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

    def __str__(self):
        return f"Dados da Conta: \nNumero: {self._numero} \nTitular: {self._nome} \nSaldo: {self._saldo} \nLimite: {self._limite}"


class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * (taxa * 2)

    def deposita(self, valor):
        self._saldo += valor - 0.10

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * (taxa * 3)

class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total
   

    def roda(self, conta):
        print("Saldo da Conta: {}".format(conta._saldo))
        self._saldo_total += conta.atualiza(self._selic)
        print("Saldo Final: {}".format(self._saldo_total))


if __name__ == '__main__':
    c = Conta('123-4', 'Joao', 1000.0, 3000)
    cc = ContaCorrente('123-5', 'José', 1000.0, 3000)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0, 3000)

    adc = AtualizadorDeContas(0.01)

    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print(f'Saldo total: {adc._saldo_total}')
    






