try:
    file = open('meu-arquivo.py')
except FileNotFoundError as exc:
    print('File not found')
    print(exc)
