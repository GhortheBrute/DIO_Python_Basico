arquivo = open(
    r"C:\Users\wilde\OneDrive - Grupo Marista\Codes\Python\DIO\Python Basico\DIO_Python_Basico\05 - Manipulação de arquivos\lorem.txt", 'r'
)

while len(linha := arquivo.readline()):
    print(linha)
    
#print(arquivo.read())
# Com readline ele devolve caracter à caracter
for line in arquivo.readline():
    print(line)
#
# # Com readlines ele devolve linha a linha
for line in arquivo.readlines():
    print(line)


arquivo.close()


