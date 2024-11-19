import matplotlib.pyplot as plt
y1 =[]           #y değerlerini depolamak için boş listeler olarak başlatılmıştır.
y2 =[]
x = range(-100,100,10)        #i, -100 ile 100 arasında 10'ar artan bir sayı aralığıdır

for i in x: y1.append(i**2)    #x içindeki her bir değerin karesi alınır ve y1 listesine eklenir. Bu, y1 = x^2 fonksiyonunu oluşturur (parabolik bir fonksiyon).
for i in x: y2.append(-i**2)

plt.plot(x,y1)   # x değerlerini ve y1 değerlerini kullanarak bir çizgi grafiği çizer. Bu, parabolik fonksiyonun grafiği olacaktır (y = x^2).
plt.plot(x,y2)
plt.xlabel("x")   #plt.xlabel("x"): X eksenine "x" etiketini ekler.
plt.ylabel("y")
plt.ylim(-2000,2000)      # plt.ylim(-2000, 2000): Y ekseninin görünür değer aralığını -2000 ile 2000 arasında sınırlar.
plt.axhline(0)          # Yatay referans çizgisi ekler. Bu çizgi, y ekseninin 0 olduğu yeri (yani, x ekseninin geçtiği yeri) belirler.
plt.axvline(0)      #  Dikey referans çizgisi ekler. Bu çizgi, x ekseninin 0 olduğu yeri (yani, y ekseninin geçtiği yeri) belirler
plt.savefig("guad.png")     # Bu komut, grafiği "guad.png" adıyla kaydeder.
plt.show()


