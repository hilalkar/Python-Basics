import numpy as np

result = np.array([1,3,5,7,9])

result =np.arange(1,10)   #1 den 9 a kadar
result =np.arange(10,100,3) # on ile yüz arasında üçer artmalı
result =np.zeros(10)
result =np.ones(10)
result =np.linspace(0,100,5) #verdiğimiz aralığı 5 e böler
result = np.linspace(0,5,5)
result = np.random.randint(0,10)  # 0 ile 10 arasında random int sayı oluşturur
np_array= np.arange(50)  #0dan 49 a kadar
np_multi = np_array.reshape(5,10) #  matris oluşturuyor satır sütun olarak
print(np_multi)
print(np_multi.sum(axis=1))   # satırların toplamını verir
print(np_multi.sum(axis=0))   #sütunların toplamını verir


rnd_numbers= np.random.randint(1,100,10) # 1 ile 100 arasında 10 tane random sayı üretir
print(rnd_numbers)
result = rnd_numbers.max(95) #üretilen sayılar arasında en yüksek sayı 95 oldu
result = rnd_numbers.min(10)

result = rnd_numbers.mean()  #üretilen sayıların ortalamasını verir
print(result)

result = rnd_numbers.argmax()  #üretilen en yüksek sayının indisini verir

print(result)






