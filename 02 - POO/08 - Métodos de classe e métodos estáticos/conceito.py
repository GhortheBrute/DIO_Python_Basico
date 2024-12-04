class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_a_partir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome,idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa("Jesus", 35)
print(p.nome, p.idade)

p2 = Pessoa.criar_a_partir_data_nascimento(1989, 12, 1, "Jesus")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(28))