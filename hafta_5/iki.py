import csv

baslik = ["sicaklik", "nem", "basinc"]

veri = [[30, 74.5, 11], [33, 96, 75]]

with open('sensor_veri.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)