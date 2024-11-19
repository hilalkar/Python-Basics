import numpy as np
# TRANSPOZE .T

a = np.arange(10).reshape(5, 2)
#10 elemanlı bir numpy dizisi oluşturur
# ardından bu diziyi reshape ile 5 satır iki sütunluk diziye dönüştürür

b = a.T
#transpoze gerçekleşir iki satırlık 5 sütunluk dizi olur

print(a)
print(b)

# MATRİSLERİN ÇARPIMI np.dot(x,y)
numpy_array = np.array([0,1,2,3,4,5,6,7,8,9])
numpy_array1 = numpy_array.reshape(5,2)
numpy_array2 = numpy_array.reshape(2,5)
print(np.dot(numpy_array1*numpy_array2))
