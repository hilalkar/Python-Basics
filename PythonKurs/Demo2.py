##Toplamda 10 sorunun sorulduğu bir sınavda her doğru cevap için 10 puan alınırken
##her yanlış cevap için -5 puan alınmaktadır. Tüm soruları cevaplayan bir kişinin doğru
##yanlış sayısı klavyeden girildiğinde toplam puanını ekrana yazan programın kodunu
##yazınız


dogru_sayisi = int(input("doğru cevap sayısını girin"))
yanlis_sayisi = int(input("yanlıs sayısını girin"))

if dogru_sayisi+yanlis_sayisi !=10:
    print(" toplam soru sayısı 10 olmalıdır ")
else:
    toplam_puan = (dogru_sayisi*10) + (yanlis_sayisi*(-5))
    print("toplam puanınız ", toplam_puan)