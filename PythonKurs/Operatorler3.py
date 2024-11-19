# 1- girilen sayının 0-100 aralığında olup olmadığını kontrol ediniz
from operator import index

sayi = float(input("sayı: "))
result = (sayi>0) and (sayi<=100)
print(f"sayı 0-100 arasında mı :{result}")

# 2- girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
sayi1= int(input("sayi : "))
sonuc = (sayi>0) and (sayi%2==0)
print(f"sayı pozitif ve çift mi :{sonuc} ")


""" 3- kullanıcıdan iki vize (%60) ve final (%40) alıp ortalama hesaplayınız
eğer ortalama 50 ve üsütyse geçti değilse kaldı yazdırın
ortalama 50 bile olsa final notu en az 50 olmalıdır 
"""
vize1 = float(input("vize1: "))
vize2 = float(input("vize2: "))
final = float(input("final: "))
ortalama = (((vize1+vize2)/2) * 0.6) + (final * 0.4)
result = (ortalama>=50) and (final>=50)
print(f"ortalamanız: {ortalama} .Dersten geçme durumunuz : {result}")


""" 4- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız 
    Formül: (kilo/boy uzunluğunun karesi)
    Aşağıdaki tabloya göre kişi hangi gruba girmektedir 
    0.0-  18.4 --> zayıf 
    18.5- 24.9 --> normal 
    25.0- 29.9 --> fazla kilolu
    30.0- 34.9 --> şişman (obez) 
"""
name = input("adınız: ")
kilo = float(input("kilo: "))
boy = float(input("boy: "))

indeks = (kilo)/(boy**2)

zayif = (index>=0) and (index<=18.4)
normal = (index>18.5) and (index<=24.9)
kilolu = (index>25.0) and (index<=29.9)
obez = (index>30.0) and (index<=34.9)

print(f"{name} kilo indeksin: {index}  \n kilo değerlendirmen:{zayif} ")
print(f"{name} kilo indeksin: {index}  \n kilo değerlendirmen:{normal} ")
print(f"{name} kilo indeksin: {index}  \n kilo değerlendirmen:{kilolu} ")
print(f"{name} kilo indeksin: {index}  \n kilo değerlendirmen:{obez} ")



