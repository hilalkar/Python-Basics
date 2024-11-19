from idlelib.colorizer import color_config

import matplotlib.pyplot as plt
#SCATTER PLOT (SERPİLME DİYAGRAMI)

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,7,6,8,9,11,12,12]

plt.scatter(x, y, label="stars",color="green", marker="*", s=30)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("my scatter plot")
plt.legend()  #çizgi türlerinin açıklanması için

plt.show()