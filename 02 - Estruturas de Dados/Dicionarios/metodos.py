# Copy
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "Telefone":"3333-2221"}
}
print(contatos)

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}
print(copia)

# Fromkeys
dicionario = dict.fromkeys(["nome", "telefone"])
print(dicionario)

dicionario_a = dict.fromkeys(["nome", "telefone"], "vazio")
print(dicionario_a)

# Get
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "Telefone":"3333-2221"}
}
print(contatos)

contatos["guilherme@gmail.com"]