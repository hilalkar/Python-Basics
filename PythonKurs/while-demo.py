sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- sayilar listesini while ile ekrana yazdır
i=0
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1


# 2- başlangıc ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
baslangic = int(input("baslangıç değeri girin: "))
bitis = int(input("bitiş değerini girin :"))
while (baslangic<bitis):
    baslangic+=1
    if(baslangic%2==1):
      print(baslangic)

# 3- 1-100 arasındaki sayıları azalan olarak yazdırın
i=100
while(i>0):
    i-=1
    print(i)

# 4- kullanıcıdan aldığınız 5 sayıyı ekranda sıralı bir sekilde yazdırın
numbers = []
i=0
while i<5:
    sayi=int(input("sayı: "))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)



# 5- kullanıcıdan alacağınız sınırsız urun bilgisini urunler listesi içinde saklayın
#    ürün sayısını kullanıcıya sorun
#    dictionary listesi yapısı (name,price) seklinde olsun
#    ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

urunler = []
adet = int(input("kaç ürün eklemek istiyorsunuz ?"))
i=0
while(i<adet):
    name = input("ürün ismi: ")
    price = input("ürün ücreti:")
    urunler.append({
        "name": name,
        "price": price
    })
    i+=1

for urun in urunler:
    print(f"ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}")
