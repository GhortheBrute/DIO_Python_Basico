def verificador_ano_bissexto():
    ano = int(input())

    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print("SIM")
            else:
                print("NÃO")
        else:
            print("SIM")
    else:
        print("NÂO")

verificador_ano_bissexto()
