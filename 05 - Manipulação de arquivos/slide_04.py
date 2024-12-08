import os
import shutil

# Criar um diretório
os.mkdir('exemplo')

# Renomear arquivos
os.rename('old.txt', 'new.txt')

# Remover um arquivo
os.remove('unwanted.txt')

# Mover um arquivo
shutil.move('source.txt', 'destination.txt')