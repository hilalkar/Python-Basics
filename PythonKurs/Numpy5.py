# numpy slicing , belirli indeksten belirli bir indekse kadar olan elemanları almak anlamına gelir
# [baslangiç : bitiş  : artış miktarı
#SLICING

import numpy as np
dizi = np.array([1,2,3,4,5,6,7,8,9,10])
print(dizi[0:5]) #dizideki elemanların ilk yarısını alır 0. indeks dahil 5 hariç

# 1-D diziler ile slicing
dizi = np.array([1,2,3,4,5,6,7,8,9,10])
print(dizi[5:])   # 5. indisten başlar sona kadar
print(dizi[:5])   # baslangictan 5.idise kadar 5 haric
print(dizi[::2])  # ne baslangıc var ne bitiş
print(dizi[1::2])  #çift sayılar isteniyor
print(dizi[-2:])   # 9 dan başlar tersine doğru hepsini alır
print(dizi[-3:-2]) # 8 den başlar 9 da biter
print(dizi[-3:2])
print(dizi[1:7:2]) # basamaklı artış


# 2-D diziler ile slicing
dizi = np.array([[1,3,5,7,9],[2,4,6,8,10]])
print(dizi[1, 1:4])   # dizinin ikinci elemanının 1. indeksten 4 ekadar
print(dizi[0:2,2]) # her iki elemanın 2. indeksteki elemanlarını alır
print(dizi[0:2 ,1:4]) # her iki elemanın 1. indeksten 4 e kadar olan elemanlarını alır




