from pathlib import Path

ROOT_PATH = Path(__file__).parent

# file = open(ROOT_PATH/'lorem.txt', 'r')
# file.close()
try:
    with open(ROOT_PATH/'lorem.txt', 'r') as file:
        print(file.read())
except IOError as exc:
    print(f'Erro ao abrir o arquivo: {exc}')

# try:
#     with open(ROOT_PATH/'arquivo-utf-8.txt','w', encoding='utf-8') as new_file:
#         new_file.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f'Erro ao abrir o arquivo: {exc}')

try:
    with open(ROOT_PATH/'arquivo-utf-8.txt','r', encoding='utf-8') as new_file:
        print(new_file.read())
except IOError as exc:
    print(f'Erro ao abrir o arquivo: {exc}')
except UnicodeError as exc:
    print(f'Erro de codificação: {exc}')

# file.read()
