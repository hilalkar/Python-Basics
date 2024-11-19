
""" Bir öğrencinin iki yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen
   not bilgisini yazdırın

   0-24-->0
   25-44-->1
   45-54-->2
   55-69-->3
   70-84-->4
   85-100-->5

"""


yazili1=float(input("1. yazılı notu: "))
yazili2=float(input("2. yazılı notu: "))
sozlu=float(input("sözlü notu: "))

ortalama = (yazili1+yazili2+sozlu)/3

if (ortalama>=0) and (ortalama<25):
    print(f"ortalamanız: {ortalama} notunuz: 0 ")
elif (ortalama>=25) and (ortalama<45):
    print(f"ortalamanız: {ortalama} notunuz: 1 ")
elif (ortalama>=45) and (ortalama<55):
    print(f"ortalamanız: {ortalama} notunuz: 2 ")
elif (ortalama>=55) and (ortalama<70):
    print(f"ortalamanız: {ortalama} notunuz: 3 ")
elif (ortalama>=70) and (ortalama<85):
    print(f"ortalamanız: {ortalama} notunuz: 4 ")
elif (ortalama>=85) and (ortalama<101):
    print(f"ortalamanız: {ortalama} notunuz: 5 ")
else:
    print("yanlış bilgi girdiniz")


