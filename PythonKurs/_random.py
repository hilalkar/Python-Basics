import random
# result=dir(random)  random modülündeki fonksiyon listesini gösterir

# result=help(random)  fonksiyonların kullanımını açıklar

result = random.random()   # 0.0 - 1.0 arasında sayı üretir
result = random.random()*100  # 0 ile 100 arasında sayı üretir
result =random.random()*10  # 0 ile 10 arasında
result = int(random.uniform(10,100))
result = random.randint(10,100)

names= ["ali","yağmur","deniz","cenk"]
result= names[random.randint(0,len(names)-1)]

greeting="hello there"
result=random.choice(greeting)      # random bir harf döndürür


liste =list(range(10))
random.shuffle(liste)  #shuffle listeyi farklı sıralar
result=liste


liste=range(100)
result = random.sample(liste,3)  #listeden random şekilde 3 sayı alırız


result = random.sample(names,2)
print(result)