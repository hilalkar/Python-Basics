from struct import pack_into

x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1- kullanıcıdan aldığınız iki sayının çarpımı ile x,y,z toplamının farkı nedir ?
a = int(input("1. sayı: "))
b = int(input("2. sayı: "))
result1 = (a*b) - (x+y+z)

# 2- y nin x e kalansız bölümünü hesaplayınız
result2 = y//x

# 3- (x,y,z) toplamının mod3 ü nedir ?
toplam = (x+y+z)
result3 = toplam%3

# 4- y nin x. kuvvetini hesaplayınız
result4 = y**x

# 5- x, *y, z =numbers işlemine göre z nin küpü kaçtır ?
#numbers = 1, 5, 7, 10, 6
x, *y, z =numbers
result5 = z**3



# 6- x, *y, z=numbers işlemine göre y nin değerleri toplamı kaçtır ?
numbers = 1, 5, 7, 10, 6
x, *y, z =numbers
toplam2 = y[0]+ y[1]+ y[2] 



