import datetime

date_str = "2023-05-01"
date_obj = datetime.datetime.strptime(date_str, "%Y-%d-%m")

print(date_obj)

data1 = datetime.datetime(2023,1,1)
data2 = datetime.datetime(2023,1,10)

print(data2 - data1)