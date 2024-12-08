import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args,**kwargs):
        print("Faz algo antes de executar a função.")
        funcao(*args,**kwargs)
        print("Faz algo depois de executar a função.")

    return envelope

@meu_decorador
def ola_mundo(nome,teste=None):
    print(f"Olá mundo {nome}!")

#ola_mundo = meu_decorador(ola_mundo)
ola_mundo("João")

print()
print(ola_mundo.__name__)