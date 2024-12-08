class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, fixo=True):
        super().__init__()
        self.fixo = fixo

    def esta_carregado(self):
        print("Não estou carregado.")


moto = Motocicleta("Azul", "ABC-1234", 2)
moto.ligar_motor()

carro = Carro("Branco", "ZPI-7584", 4)

caminhao = Caminhao(
    "Laranja",
    "LSI-4825",
    8,
)
caminhao.esta_carregado()
