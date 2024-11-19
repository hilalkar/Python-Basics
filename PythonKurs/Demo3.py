#İkinci dereceden bir bilinmeyenli bir denklemin delta değerini hesaplayan ve bu
#değere göre denklemin köklerini ekrana yazan uygulamanın kodunu yazınız.
import math

# kullanıcıdan denklem katsayıları alınır
a=float(input("a katsayısını girin"))
b=float(input("b katsayısını girin"))
c=float(input("c katsayısını girin"))

#delta hesaplanır
delta = b**2 - 4*a*c
print("delta değeri: ",delta)

#delta değerine göre kökleri hesapla
if delta > 0:
    #iki farklı reel kök vardır
    x1= (-b + math.sqrt(delta)) / (2*a)
    x2= (-b - math.sqrt(delta)) / (2*a)
    print(f"iki tane reel kök vardır x1= {x1} , x2= {x2} " )
elif delta==0:
    #çift katlı bir tane kök vardır
    x= -b / (2*a)
    print(f" çift katlı tek kök vardır  x= {x}")
else:
    #gercek kök yok karmşık kökler var
    gercek_kismi= -b/(2*a)
    imajiner_kismi= math.sqrt(-delta) / (2*a)
    print(" gercek kök yoktur karmasık kökler vardır")
    print("x1 =",gercek_kismi,"+",imajiner_kismi,"i")
    print("x2 =", gercek_kismi, "+", imajiner_kismi,"i")