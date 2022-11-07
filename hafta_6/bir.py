"""
1- veri isimli bir klasör oluşturun
2- zip dosyasını veri klasörüne çıkartın
3- zip dosyası içindeki csv dosyalarının tüm içeriğini tek bir csv dosyasında birleştirin, volume olmasın
4- bu kayıtların tamamını sqlite veri tabanına bir tablo oluşturarak yükleyin
5- kullanıcının belirlediği paritenin, aralığının, değerin grafiğini çizdirin
"""
import os
import zipfile
import pandas as pd
import sqlite3

if not os.path.exists("veri"):
    os.mkdir('veri')
    arsiv = zipfile.ZipFile('pariteler_cikti_1hour_2022_2022.zip')    
    arsiv.extractall("veri/")
    
    tum_dosyalar = os.listdir("veri")
    pandas_csv_listesi = []
    for csv_dosya in tum_dosyalar:
        veri = pd.read_csv("veri/" + csv_dosya)
        del veri["volume"] #volume sütunu silmek için
        pandas_csv_listesi.append(veri)
        
    birlesmis_csv_ler = pd.concat(pandas_csv_listesi)
    birlesmis_csv_ler.to_csv('hepsi.csv', index=False)    
    print(birlesmis_csv_ler)
    
bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor()
cursor.execute("CREATE TABLE IF NOT EXIST parite("
    + "id  INTEGER PRIMARY KEY AUTOINCREMENT,"
    + "otime DATETİME, open FLOAT"
    + "high FLOAT, low FLOAT, close FLOAT);")   

cursor.execute("INSERT INTO "
               +"parite(otime, open, high, low, close)"
               +"'2022-01-01 03:00:00',"
            ) 

bag.commit()
bag.close()
kayitlar = pd.read_csv("hepsi.csv")