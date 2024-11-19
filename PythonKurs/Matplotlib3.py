import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
#plt.ylabel('some numbers') ifadesi, y eksenine "some numbers" şeklinde bir etiket ekler.
# Bu etiket, grafikte y ekseninin neyi temsil ettiğini açıklamak için kullanılır.
plt.show()



# Eğer yalnızca y verisi sağlarsanız, Matplotlib otomatik olarak x eksenini sırasıyla 0, 1, 2, 3, ... olarak kabul eder
# Bu, varsayılan davranıştır çünkü Matplotlib, her y değeri için bir x değeri eşleştirmeyi bekler.
# Eğer x eksenine herhangi bir değer vermezseniz, Matplotlib bu x değerlerini otomatik olarak oluşturur
# ve sırasıyla (başlangıç olarak 0'dan başlayarak) her bir y değerine bir x değeri atar.