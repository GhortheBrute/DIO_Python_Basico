a = set([1, 2, 3, 1, 3, 4])
print(a)
print()


b = set("abacaxi")
print(b)
print()


c = set(("palio", "gol", "celta", "palio"))
print(c)
print()


# Converter SET para LISTA
#lista = list(a)
print(list(a))
print()


# Enumerate
for indice, carro in enumerate(c):
    print(f"{indice}: {carro}")
print()

# Métodos de SET

# Union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print("Union ",conjunto_a.union(conjunto_b))
print()


# Intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print("Intersection ",conjunto_a.intersection(conjunto_b))
print()


# Difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print("Difference A B",conjunto_a.difference(conjunto_b))
print("Difference B A",conjunto_b.difference(conjunto_a))
print()


# Issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print("Issubset A B ",conjunto_a.issubset(conjunto_b))
print("Issubset B A ",conjunto_b.issubset(conjunto_a))
print()


# Issuperset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print("Issuperset A B ",conjunto_a.issuperset(conjunto_b))
print("Issuperset B A ",conjunto_b.issuperset(conjunto_a))
print()
# Isdisjoint
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print("Isdisjoint A B ",conjunto_a.isdisjoint(conjunto_b))
print("Isdisjoint A C ",conjunto_a.isdisjoint(conjunto_c))
print()

# Add
sorteio = {1, 23}

print(sorteio)
sorteio.add(25)
print(sorteio)

# Copy
sorteio_1 = {1, 23}
print(sorteio_1)

sorteio_2 = sorteio_1.copy()
print(sorteio_2)

# Discard
numeros = {1 ,2 ,3 , 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)

numeros.discard(1)

print(numeros)

numeros.discard(45)

print(numeros)

# Pop
numeros = {1 ,2 ,3 , 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)

numeros.pop()

print(numeros)

numeros.pop()

print(numeros)

# Remove
numeros = {1 ,2 ,3 , 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)

numeros.remove(1)

print(numeros)

numeros.remove(2)

print(numeros)