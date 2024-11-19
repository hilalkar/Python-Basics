"""
   ogrenciler = {
       "120" : {
           "Ad" : "Ali"
           "Soyad" : "Yılmaz"
           "Telefon" : "532 000 00 01"
       },
       "125" : {
           "Ad" : "Can"
           "Soyad" : "Korkmaz"
           "Telefon" : 532 000 00 02"
       },
       "128" : {
           "Ad" : "Volkan"
           "Soyad" : "Yükselen"
           "Telefon" : 532 000 00 03"
       },
   }

"""

""" 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız 
       bilgilerle dictionary içinde saklayın


     2- Öğrenci numarasını kullanıcdan alıp
        ilgili öğrenci bilgisini gösterin
 """

ogrenciler = {}

number = input(" öğrenci no: ")
name = input("öğrenci ismi: ")
surname = input("öğrenci soyismi: ")
phone = input(" öğrencinin telefon numarası: ")

ogrenciler[number] = {
     "ad" : name,
     "soyad": surname,
     "telefon": phone
 }
print(ogrenciler)

ogrenciler.update({
     number: {
     "ad" : name,
     "soyad": surname,
     "telefon": phone
     }
}
)
ogrenciler.update({
     number: {
     "ad" : name,
     "soyad": surname,
     "telefon": phone
     }
 })
ogrenciler.update({
     number: {
     "ad" : name,
     "soyad": surname,
     "telefon": phone
     }
 })
print(ogrenciler)

# 2.soru
ogrNo = input("öğrenci no: ")
ogrenci=ogrenciler[number]
print(ogrenci)

print("*" * 50)








