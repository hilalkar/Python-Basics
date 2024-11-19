"""
 1 - 100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın (hak=5)
 ** Random modülü için python random şeklinde arama yapın
 ** 100 üzerinden puanlama yapın her soru 20 puan
 ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden olsun

"""

import random

sayi = random.randint(1,100)
can= int(input(" kaç tane hak kullanmak istersiniz ?"))
sayac = 0

while can>0:
    can-=1
    sayac+=1
    tahmin = int(input(" tahmin edilen sayıyı giriniz \n"))

    if sayi==tahmin:
        print(f"Tebrikler {sayac} denemede buldunuz. Toplam puanınız {100 - ((sayac-1)*(100/can))} ")
    elif sayi>tahmin:
        print(" yukarı ")
    else :
        print(" aşağı ")

    if can==0:
        print(f"Hakkınız bitti tutulan sayı : {sayi} ")








