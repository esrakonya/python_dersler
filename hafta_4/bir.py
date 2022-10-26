# Kendisine gönderilen sayılardan sadece palindrom (909, 888) olanları toplayan diğerlerini de bu toplamdan çıkaran
# ve döndüren fonksiyonu yazınız.




def palindrom (*sayi):
    toplam = 0
    for number in sayi:
        
        if str(number) == str(number)[::-1]:
            toplam += number
        else:
            toplam -= number
    return toplam             
    

print(palindrom(10, 101, 55, 40, 909)) 