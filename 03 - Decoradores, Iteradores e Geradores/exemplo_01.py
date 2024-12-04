def dizer_oi(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python juntos!"

def mensagem_para_jesus(funcao_mensagem):
    return funcao_mensagem("Jesus")

print(mensagem_para_jesus(dizer_oi))
print(mensagem_para_jesus(incentivar_aprender))
