import matplotlib.pyplot as plt
# BAR GRAPHS

values = [5,6,3,7,2]      #  Bu liste, çubuk grafikteki her bir çubuğun yüksekliğini belirler. Yani, her bir kategoriye karşılık gelen değeri içerir. Bu durumda 5, 6, 3, 7 ve 2'yi temsil eder.
names = ["A", "B" , "C" , "D", "E"] #X ekseninde: "A", "B", "C", "D" ve "E" etiketleri yer alacak.

plt.bar(names, values , color="green")   # bu komut çubuk grafiği çizer
plt.show()