from operator import length_hint

website= "http://www.sadıkturan.com"
course= "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1-  "course" karakter dizisinde kaç tane karakter bulunmaktadır ?
result1 = len(course)
length = len(website)
print(result1)

# 2-  "website" içinden www karakterlerini alın
result2 = website[7:10]
print(result2)

# 3-  "website" içinden com karakterlerini alın
result3 = website[22:25]
result = website[length-3:length]
print(result3)

# 4-  "course" içinden ilk 15 ve son 15 karakteri alın
result4 = course[0:15]
result5 = course[result1-15:]
print( result4 +" "+ result5)


# 5-  "course" ifadesindeki karakterleri tersten yazdırın
result6 = course[::-1]
print(result6)

name, surname, age, job='Bora', 'Yılmaz', "32", 'mühendis'

# 6- yukarıda verilen değişkenleri kullanarak "benim adım Bora Yılmaz yaşım 32 ve mesleğim mühendis" ifadesini yazdırın
result7 = "Benim adım "+ name+" "+surname+ " yaşım "+age+ " ve mesleğim "+ job
print(result7)
res = "benim adım {0} {1} yaşım {2} ve mesleğim {3}".format(name,surname,age,job)
print(res)


# 7- "Hello world" ifadesindeki w harfini W ile gösteriniz
s = "Hello world"
result8 = s[0:6] + "W" +s[-4:]
print(result8)
s1 = s.replace("w","W")
print(s1)


# 8- "abc" ifadesini yan yana 3 kere yazdırın
result9 = "abc " * 3
print(result9)
