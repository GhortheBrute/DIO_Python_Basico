numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

pares_2 = [numero for numero in numeros if numero % 2 == 0]
print(pares_2)

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

quadrado_2 = [numero ** 2 for numero in numeros]
print(quadrado_2)