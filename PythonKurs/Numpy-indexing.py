import numpy as np

from Math import value

#numbers =np.array([0,5,10,15,20,25,50,75])
#result = numbers[5]
#result = numbers[-1] # en sağdan
#result = numbers[0:3]
#result = numbers[:3]
#result = numbers[3:]
#result = numbers[::]
#result = numbers[::-1]  # 75 ten geriye doğru başlar hepsini yazdırır

numbers2 = ([[0,5,10],[15,20,25],[50,75,85]])     #liste olarak tanımlandığı için matris[][] şeklinde erişim yapıyoruz
#result = numbers2[0] # 0. indiste olan dizi
#result = numbers2[0][2] # 0. indiste olan dizinin ikinci indeksteki elemanı liste olarak tanımlandığı için matris[][] şeklinde erişim yapıyoruz
#result = numbers2[:][2] # sadece numbers2'nin 2. indeksteki alt listesini ([50, 75, 85]) döndürür
#result = [row[2] for row in numbers2]  # Her satırın 2.indeis elemanını alır
#result = numbers2[-1][:] # satırdaki son diziden başlar ve o diziyi alır
#result = numbers2[:3][:3] # 3.indise kadar olan iki diziyi alır ve tüm kolonları alır
#result = [row[:2] for row in numbers2[:2]] # 1. ve 2. indisteki iki diziyi alır ve onların ilk iki elemanını döndürür


print(numbers2)
print(result)




