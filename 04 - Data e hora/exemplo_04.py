from datetime import datetime, timezone, timedelta

import pytz

data = datetime.now(pytz.timezone('Europe/Oslo'))
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))

print(data)
print(data2)

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)