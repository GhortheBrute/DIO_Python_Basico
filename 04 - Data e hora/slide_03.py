import datetime

d = datetime.datetime.now()

print(d.strftime("%d/%m/%Y %H:%H"))

date_string = "20/07/2023 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)