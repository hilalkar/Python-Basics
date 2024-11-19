"""
Girilen bir sayının asal olmadığını bulun
** Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir
"""

sayi = int(input(" Sayıyı giriniz: "))

asalMi = True

if sayi==1:
    asalMi=False
    print(" Sayı asal değildir ")

for i in range(2,sayi):
    if (sayi%i==0):
        asalMi=False
        break

if asalMi:
    print("Sayı asaldır ")
else:
    print("sayı asal değildir ")

