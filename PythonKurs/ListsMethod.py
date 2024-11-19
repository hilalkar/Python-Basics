from operator import index
from traceback import print_tb

names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1- cenk ismini listenin sonuna ekleyiniz
names.append("Cenk")
print(names)
# 2- sena değerini listenin başına ekleyiniz
names.insert(0,"Sena")
print(names)

# 3- deniz ismini listeden siliniz
names.remove("Deniz")
names.pop()
print(names)

# 3- deniz isminin indexi nedir
indeks=names.index("Deniz")
names.pop(indeks)
print(names)

# 4- ali listenin elemanı mıdır
result = "Ali" in names
print(result)

# 5- liste elemanlarını ters cevirin
names.reverse()
print(names)

# 6- liste elemanlarını alfabetik olarak sıralayın
names.sort()
print(names)

# 7- years listesini rakamsal olarak büyüklüğe göre sıralayın
years.sort()
print(years)

# 8- str = "Chevrolet,Dacia" karakter dizisini listeye cevirin
str = "Chevrolet,Dacia"
result = str.split(",")
print(result)

# 9- years dizisinin en büyük ve en küçük elemanı
min = min(years)
max = max(years)
print(min,max)

# 10- years dizisinde kaç tane 1998 değeri var
result = years.count(1998)
print(result)

# 11- years dizisinin tüm elemanlarını siliniz
del years

# 12- kullanıcıdan alacağınız 3 tane markayı bir listede saklayın
markalar = []
marka = input("Marka: ")
markalar.append(marka)
marka= input("Marka: ")
markalar.append(marka)
marka= input("Marka: ")
markalar.append(marka)
print(markalar )
