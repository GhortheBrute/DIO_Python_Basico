from datetime import datetime, timedelta, timezone, date, time

tipo_carro = 'G'    # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now(timezone.utc)

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(days=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}.')
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}.')
else:
    data_estimada = data_atual + timedelta(days=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}.')

print("Data de hoje subtraindo 1 dia.")
print(date.today() - timedelta(days=1))

print("Hora 14:22:48 subtraída de 1 hora")
resultado = datetime(2024, 12, 8, 14, 22, 48) - timedelta(hours=1)
print(resultado.time())

print("Data atual")
print(datetime.now().date())