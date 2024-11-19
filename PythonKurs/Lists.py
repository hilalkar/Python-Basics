from typing import List

from KarakterDizileri import result  # 1- "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz
arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']

 # 2- liste kaç elemanlıdır
result = len(arabalar)

 # 3- listenin ilk ve son elemanı nedir
result = arabalar[0]
result = arabalar[3]

 # 4- mazda değerini toyota ile değiştirin
arabalar[3] = "Toyota"
result = arabalar

 # 5- mercedes listenin elemanı mıdır
result = "Mercedes" in arabalar

 # 6- listenin -2 indeksindeki değer ne
result = arabalar[-2]

 # 7- listenin ilk üç elamanını alın
result = arabalar[0:3]

 # 8- listenin sonn iki elemanı yerine toyota ve renault değerlerini ekleyin
arabalar[-2:] = ["Toyota", "Renault"]

 # 9- listenin üzerine audi ve nissan değerlerini ekleyin
result = arabalar + ["Audi","Nissan"]

 # 10-listenin son elemanını silin
del arabalar[-1]
result = arabalar

 # 11-liste elemanlarını tersten yazdırın
result = arabalar[::-1]

 # 12- aşağıdaki verileri liste içinde saklayın
     # studentA = Yiğit Bilgi 2010 (70,60,70)
     # studentB = Sena Turan 1999 (80,90,70)
     # studentC = Ahmet Turan 1998 (80,70,90)

studentA= ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Yiğit", "Bilgi", 1999, [80, 90, 70]]
studentC = ["Ahmet", "Turan", 1998, [80, 70, 90]]

# 13- liste elemanlarını ekrana yazdırın
result = studentA[]
result = studentB[]
result = studentC[3][1]

print(result)
