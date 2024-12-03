def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
#TODO: Itere através de cada caractere na string string.
    for letra in string:
#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
        if not(letra in contador):
            contador[letra] = 1
        else:
            contador[letra] += 1
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)