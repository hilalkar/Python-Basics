""" Kullanıcıdan isim yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz
    yaş en az 18 ve eğitim durumu lise ya da üniversite olmalıdır
"""
isim = input("isim: ")
yas = int(input("yaş: "))
egitim = input("eğitim: ")

if (yas>18):
    if  (egitim=="lise" or egitim=="üniversite"):
         print(f"{isim} Ehliyet alabilirsin ")
    else:
         print(f"{isim} Ehliyet alamazsınız eğitim durumunuz yetersiz ")
else :
    print(f"{isim} Ehliyet alamazsınız yaşınız tutmuyor ")

