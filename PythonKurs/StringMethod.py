from traceback import print_tb

website= "http://www.sadıkturan.com"
course= "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- " Hello world " ifadesinde baştaki ve sondaki boşluk karakterlerini silin
result = " Hello world ".strip()
result = " Hello world ".lstrip()
result = " Hello world ".rstrip()   #right sağdakileri siler





# 2- "www.sadıkturan.com" ifadesinde sadıkturan bilgisi haricindeki tüm karakterleri silin
result = "www.sadıkturan.com".strip("w.moc")



# 3- course karakter dizisinde tüm harfleri küçük yapın
result = course.lower()


# 4- website içinde toplam kaç tane a harfi vardır ( count("a") )
result = website.count("a")



# 5- website "www" ile başlayıp "com" ile bitiyor mu
result = website.startswith("www")
result = website.endswith("com")



# 6- website içinde ".com" ifadesi var mı
result = website.find(".com")


# 7- course içindeki karakterlerin hepsi alfabetik mi (isalpha , isdigit)
result = course.isalpha()
result = "123".isdigit()


# 8- contents kelimesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
result = "contents".center(50,"*")



# 9- course karakter dizisindeki tüm boşluk karakaterlerini "-" ile değiştirin
result = course.replace(" ","-")

# 10- "Hello world" karkater dizisinde world kelimesini "there "ile değiştirin
result = "Hello world".replace("world" ,"there")


# 11- course karakter dizisini boşluk karakerlerinden ayırın
result = course.split(" ")



print(result)






