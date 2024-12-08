import csv

with open('example.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# with open('example.csv','w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['nome', 'idade'])
#     writer.writerow(['Ana', 30])
#     writer.writerow(['João', 25])