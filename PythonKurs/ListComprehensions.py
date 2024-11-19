# 1- range() aralık tutar 0-9 dahildir 1. yol
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers )

# 2- 2.yol for döngüsü ile gezilen elemanlar numbers list de tutulur
numbers = [x for x in range(10)]
print(numbers)

# 3-
sayilar = [ x**2 for x in range(5)]
print(sayilar)

kare = [ x*x for x in range(5)]
print(kare)

# 4- üçe tam bölünen x sayılar
dizi = [ x*x for x in range(5) if x%3==3]
print(dizi)

# 5- string örneği
myString = "hello"
mylist = [letter for letter in myString]
print(mylist)

# 6-
years = [1983, 1999, 2002, 2013]
age = [2024 - year for year in years ]
print(age)

# 7-
results = [x if x%2==0 else "tek" for x in range(10)]
print(results)

# 8-1.
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

# 8-2.

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)






