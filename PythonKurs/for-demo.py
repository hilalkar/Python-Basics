sayilar =[1, 3, 5, 7, 9, 12, 19, 21]

# 1- hangi sayılar 3 ün katıdır ?
for sayi in sayilar:
   if(sayi%3==0):
       print(sayi)


# 2- sayılar listesindeki sayıların toplamı kaçtır ?
toplam = 0
for sayi in sayilar:
    toplam +=sayi
print("Toplam: " ,toplam)


# 3- sayılar listesindeki tek sayıların karesini alın
for sayi in sayilar:
    if(sayi%2==1):
        print(sayi**2)


sehirler = ["Kocaeli", "İstanbul", "Ankara", "İzmir", "Rize"]
# 4- sehirlerden hangisi en fazla 5 karakterlidir ?
for sehir in sehirler:
   if(len(sehir)<=5):
       print(sehir)


urunler = [
    { "name": "Samsung s6", "price":3000},
    { "name": "Samsung s7", "price":4000},
    { "name": "Samsung s8", "price":5000},
    { "name": "Samsung s9", "price":6000}
]

# 5- ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])
    toplam+=fiyat
print("toplam ürün fiyatı:", toplam)


# 6- ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz
for urun in urunler:
    if(int(urun["price"] <= 5000)):
        print(urun["name"])








