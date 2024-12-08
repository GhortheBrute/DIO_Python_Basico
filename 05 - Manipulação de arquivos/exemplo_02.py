file = open(
    r'C:\Users\wilde\OneDrive - Grupo Marista\Codes\Python\DIO\Python Basico\DIO_Python_Basico\05 - Manipulação de arquivos\teste.txt', 'w'
)
file.write('Escrevendo teste de palavras.')
file.writelines(["\nescrevendo ", "\num ", "\nnovo ", "\ntexto."])
file.close()