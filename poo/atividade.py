class BombaCombustivel:

    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel) -> None:
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__quantidade_combustivel =  quantidade_combustivel
    
    
    def abastecerporValor(self, valor_abastecido, carro): 
        if carro.get_tipo_combustivel() == self.__tipo_combustivel:
            carro.set_quantidade_litro(valor_abastecido / self.__valor_litro)
            self.__quantidade_combustivel -= valor_abastecido / self.__valor_litro
            return valor_abastecido / self.__valor_litro
        else:
            self.__tipo_combustivel = carro.tipo_combustivel
            carro.quantidade_litros += valor_abastecido / self.valor_litro
            self.__quantidade_combustivel -= valor_abastecido / self.valor_litro
            return valor_abastecido / self.__valor_litro


    def get_quantidade_combustivel(self):
        return self.__quantidade_combustivel

    def abastecerporLitro(self, litros, carro):
        if carro.get_tipo_combustivel() == self.__tipo_combustivel:
            carro.set_quantidade_litro(litros * self.__valor_litro)
            self.__quantidade_combustivel -= litros
            return litros * self.__valor_litro
        else:
            carro.quantidade_litros += litros * self.__valor_litro
            self.__quantidade_combustivel -= litros
            return litros * self.__valor_litro
    
    def alterarvalor(self, novoValor):
        self.__valor_litro = novoValor
    
    def alterarCombustivel(self, tipo_combustivel):
        self.__tipo_combustivel = tipo_combustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.__quantidade_combustivel = novaQuantidade



class Veiculo():

    def __init__(self, tipo_veiculo, tipo_combustivel, quantidade_litro):
        self.__tipo_veiculo = tipo_veiculo 
        self.__tipo_combustivel = tipo_combustivel
        self.__quantidade_litro = quantidade_litro

    def get_tipo_veiculo(self):
        return self.__tipo_veiculo

    def set_tipo_veiculo(self, novo_veiculo):
        self.__tipo_veiculo = novo_veiculo

    def get_tipo_combustivel(self):
        return self.__tipo_combustivel

    def set_tipo_combustivel(self, novo_combustivel):
        self.__tipo_combustivel = novo_combustivel

    def get_quantidade_litro(self):
        return self.__quantidade_litro

    def set_quantidade_litro(self, nova_quantidade_litro):
        self.__quantidade_litro = nova_quantidade_litro
        


    
        

bomba1 = BombaCombustivel('gasolina', 5.55, 100)
bomba2 = BombaCombustivel('alcool', 4.58, 100)
veiculo1 = Veiculo('Carro', 'alcool', 15)
Veiculo2 = Veiculo('moto','gasolina', 5)
bomba2.abastecerporLitro(5, veiculo1)
bomba1.abastecerporValor(20, Veiculo2)