import matplotlib.pyplot as plt
import numpy as np
#DENKLEMİN GRAFİĞİNİ ÇİZME

x= np.arange(0, 2*(np.pi), 0.1)  #0 ile 2𝜋 arasında 0.1 aralığında değerler oluşturan bir NumPy dizisi oluşturur.

y= np.sin(x)  # dizisindeki her bir değerin sinüsünü hesaplar ve sonuçları y dizisine atar.
plt.plot(x,y)
plt.show()