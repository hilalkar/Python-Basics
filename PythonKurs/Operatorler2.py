# 1- girilen iki sayıdan hangisi büyüktür
a = int(input("a: "))
b = int(input("b: "))
result = (a>b)
print(f"a: {a} b: {b} den büyüktür:{result}")


""" 2- kullanıcıdan iki vize (%60) ve final (%40) alıp ortalama hesaplayınız
eğer ortalama 50 ve üsütyse geçti değilse kaldı yazdırın """
vize1 = float(input("vize1: "))
vize2 = float(input("vize2: "))
final = float(input("final: "))
ortalama = (((vize1+vize2)/2) * 0.6) + (final * 0.4)
print(f"ortalamanız: {ortalama} .Dersten geçme durumunuz : {ortalama>=50}")



# 3- girilen bir sayı tek mi çift mi onu yazdırın
sayi = int(input("sayi: "))
result = (sayi%2==0)
print(f"girilen sayının tek çift olma durumu {result} ")


# 4- girilen bir sayının pozitif negatif olduğunu yazdırın
sayi1 =int(input("sayi1: "))
isPositive = (sayi1>0)
print(f"sayının pozitif olma durumu :{isPositive}")


# 5- parola ve e mail bilgisini isteyip doğruluğunu kontrol edin (email: email@hilalkar.com parola:abc123)
email = "email@hilalkar.com"
parola = "abc123"

girilenEmail = input("email : ")
girilenParola = input("parola: ")

isMail = (email==girilenEmail)
isParola = (parola==girilenParola)

print(f"Mail doğruluk durumu: {isMail} /n Parola doğruluk durumu : {isParola} ")

