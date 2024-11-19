import matplotlib.pyplot as plt
#SCATTER PLOTS (DAĞILIM GRAFİĞİ)

x_values = [0,1,2,3,4,5]
y_values = [0,1,4,9,16,25]

plt.scatter(x_values, y_values , s=30 , color="blue")
# s=30: Her noktanın boyutunu belirler; burada 30 birimlik bir boyut seçilmiştir.
# Bu satır, dağılım grafiğini çizer . bir nevi nokta grafiği

plt.show()

