
liste =["1","2","5a","10b","abc","10","50"]
# 1- liste elemanları içindeki saysıal değerleri bulunuz
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue


# 2- kullanıcı q değerini girmedikçe her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazdırınız
while True:
    sayi=input("Sayı:")
    if sayi == "q":
        break
    try:
        result = float(sayi)
        print("girdiğiniz sayı", result)
    except ValueError:
        print("geçersiz sayı ")
        continue

# 3- girilen parola içinde türkçe karakter hatası veriniz

turkce_karakterler= "şçğüöıİ"
parola = input("parolayı giriniz")
for i in turkce_karakterler:
    if i in turkce_karakterler:
        raise TypeError(" parola türkçe karakter içeremez")
    else:
        pass
print("geçerli parola")

# 4- faktöriyel fonksiyonu oluşturup fonskiyona gelen değerler için hata mesajları verin

def faktoriyal(x):
    x=int(x)

    if x<0:
        raise ValueError("negatif değer ")
    result = 1

    for i in range(1,x+1):
        result*=i
    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y=faktoriyal(x)
    except ValueError:
        print(ValueError)
        continue

print(y)
