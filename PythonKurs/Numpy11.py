import numpy as np

# İlk olarak 3x5 boyutunda bir NumPy dizisi oluşturuluyor
e=np.array([[1,2,3,4,5],[4,5,6,7,8],[1,3,5,7,9]])
print("orijinal e array:")
print(e)


# e dizisinin üst ve altına 0 satırları ekleniyor
f=np.concatenate((np.zeros((1,e.shape[1])),e,
                   np.zeros((1,e.shape[1]))),axis=0)
print("\n alt ve üste 0 satırları eklendikten sonra \n")
print(f)

# f dizisinin sağına ve soluna sıfır sütunları ekleniyor
g=np.concatenate((np.zeros((f.shape[0],1)),f,
                   np.zeros((f.shape[0],1))),axis=1)
print("\n sağ ve sola 0 satırları eklendikten sonra \n")
print(g)

#matrisin sağ sol alt üst kısımlarına 0 dan oluşan çerçeve ekleyen kod
#e.shape[0] satır sayısını e.shape[1] sütun sayısını verir
# np.zeros((1, e.shape[1])) e ile aynı sütun sayısına (yani 5 sütun ) sahip bir sıfır satırı oluşturur [0, 0, 0, 0, 0] gibi
# np.concatenate fonksiyonunu axis=0 eksneinde kullanarak sıfır satırı , e ve diğer sıfır satırını üst üste ekliyoruz
# np.zeros((f.shape[0], 1)), f dizisi ile aynı satır sayısına (5 satır) sahip, bir sütunluk sıfır sütunu oluşturur.
# np.concatenate fonksiyonunu axis=1 ekseninde kullanarak sıfır sütununu, f dizisini ve diğer sıfır sütununu yan yana ekliyoruz.