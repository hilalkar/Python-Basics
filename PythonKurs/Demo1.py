# 1) 1’den 10’a kadar olan sayıların toplamı
sum_all = sum(range(1, 11))
print("1'den 10'a kadar olan sayıların toplamı:", sum_all)

# 2) 1’den 10’a kadar olan tek sayıların toplamı
sum_odds = sum(i for i in range(1, 11) if i % 2 != 0)
print("1'den 10'a kadar olan tek sayıların toplamı:", sum_odds)

# 3) 1’den 10’a kadar olan tek ve çift sayıların ayrı ayrı toplamı
sum_evens = sum(i for i in range(1, 11) if i % 2 == 0)
print("1'den 10'a kadar olan tek sayıların toplamı:", sum_odds)
print("1'den 10'a kadar olan çift sayıların toplamı:", sum_evens)

# 4) Kullanıcının girdiği sayının rakamlarının toplamı
number = int(input("Bir sayı girin: "))
digit_sum = sum(int(digit) for digit in str(number))
print("Girdiğiniz sayının rakamlarının toplamı:", digit_sum)

# 5) Girilen sayının faktöriyelini hesaplama
def factorial(n):
    if n < 0:
        return "Negatif sayının faktöriyeli tanımsızdır."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
print(f"{number} sayısının faktöriyeli:", factorial(number))
