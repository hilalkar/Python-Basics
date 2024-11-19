# 1- gönderilen kelimeyi ekranda belirtilen kez ekranda gösteren fonksiyonu yazın
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir("merhaba \n",10)


# 2- kendine gönderilen sınırsız sayıdaki parametreyi bir listeye ceviren fonksiyonu yazın
# parametrenin önünde * olması sonsuz parametre olduğunu temsil eder
def listeyecevir(*params):
    liste = []

    for param in params:
        liste.append(param)
    return liste
print(listeyecevir(13,13,2,3,2,3,4,3,))

# 3- gönderilen iki sayı arasındaki asalları bulun
sayi1 = int(input("sayı 1:"))
sayi2 = int(input("sayı 2:"))

def asalBul (sayi1,sayi2):
    for i in range(sayi1, sayi2+1):
        if i>1:
            for j in range(2,i):
                if (i%j==0):
                    break
                else:
                    print(i)


