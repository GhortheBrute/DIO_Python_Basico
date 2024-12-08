import datetime

import pytz

d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)

d = datetime.datetime.now(pytz.timezone("US/Eastern"))
print(d)

d = datetime.datetime.now(pytz.timezone("UTC"))
print(d)