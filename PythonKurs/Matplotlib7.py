import matplotlib.pyplot as plt
# BAR GRAPHS (yatay olarak çevrilmiş )
values = [5,6,3,7,2]
names = ["A", "B" , "C", "D","E"]
plt.barh(names, values, color="yellowgreen")  #Bu komut, yatay çubuk grafiği çizer.
plt.show()
