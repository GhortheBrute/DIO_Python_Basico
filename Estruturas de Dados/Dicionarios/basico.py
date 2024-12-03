pessoa = {"nome": "Guilherme", "idade": 28}

print(pessoa)

basico = dict(nome="Guilherme", idade=45)
print(basico)

pessoa["Telefone"] = "3333-1234"

print(pessoa)

contatos = {
    "fulano@email.com": {"nome":"Fulano","Telefone":12345678},
    "ciclano@email.com": {"nome":"Ciclano","Telefone":87654321},
    "maria@email.com": {"nome":"Maria","Telefone":98765432},
    "jose@email.com": {"nome":"Jose","Telefone":23456789},
}
print(contatos)

for chave, itens in contatos.items():
    print(chave, itens)
