# map() bir list ve fonksiyonu beraber kullanmayı sağlar

def square(num): return num**2
numbers = [1,3,4,5]
# result = list(map(square,numbers))
#fonksiyon map içinde tanımlandı ek olarak oluşturulmadı
result = list(map(lambda num: num**2 ,numbers))
print(result)



def check_even(num): return num%2==0
# result = list(filter(check_even,numbers))
result = list(filter(lambda num: num%2==0 ,numbers))
