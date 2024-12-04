class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("FOM! FOM!")

    def parar(self):
        print("A bicicleta parou!")

    def correr(self):
        print("A bicicleta está andando.")

    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

joao = Bicicleta("Vermelha","XRS-39",2024, 149.90)

joao.buzinar()

joao.parar()

joao.correr()

print(joao)