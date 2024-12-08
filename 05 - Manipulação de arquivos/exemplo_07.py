import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH/'usuarios.csv','w', encoding='utf-8',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id','nome'])
        writer.writerow(['1', 'Maria'])
        writer.writerow(['2', 'João'])
except IOError as exc:
    print(f'Erro ao criar o arquivo {exc}')

# try:
#     with open(ROOT_PATH/'usuarios.csv','r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row)
#
# except IOError as exc:
#     print(f'Erro ao ler o arquivo {exc}')

try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            # print(f'ID: {row['id']}')
            # print(f'Nome: {row['nome']}')

except IOError as exc:
    print(f'Erro ao ler o arquivo {exc}')