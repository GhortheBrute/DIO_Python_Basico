lista = [1, "Python", [40, 30, 20]]
# Copy
lista2 = lista.copy()

print(lista)
print(lista2)

# Count
print(lista.count("Python"))

# Extend
lista2.extend(["java","csharp"])
print(lista2)

# Index
print(lista2.index("java"))

# Pop
lista2.pop()
print(lista2)

# Remove
lista2.remove("java")
print(lista2)

# Reverse
lista2.reverse()
print(lista2)

# Sort
#lista2.sort()
print(lista2)

#lista.sort(reverse=True)
print(lista)


numeros = [[n**2 if n > 6 else n for n in range(10) if n % 2 == 0]]

print(numeros)








