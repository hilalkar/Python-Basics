#toplamda 3 cevap hakkı verilen bir sayı tahmin oyununda;
# Yarışmacı sayıyı doğru tahmin ettiğinde kaçıncı hakkında doğru tahmin ettiği ile
#birlikte ekrana yazan ve programı sonlandıran, (Örnek Çıktı: 2. Tahminde bildiniz)
# 3 hakkında da doğru tahmin edemeyen yarışmacıya “Doğru tahmin yapamadınız” mesajı
#veren programın kodunu yazınız.

import random

dogru_sayi=random.randint(1,10)
for hak in range(1,4):
    tahmin= int(input(f" {hak}. tahmininizi girin"))

    if tahmin==dogru_sayi:
        print(f" {hak}.tahminde bildiniz")
        break
    else:
        print("yanlıs tahminde bulundunuz")
else:
    print("doğru tahmin yapamazdınız doğru sayı=",dogru_sayi)
