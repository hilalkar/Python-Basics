import numpy as np
numpy_array1=np.array([0,1,2,3,4,5,6,7,8,9])
numpy_array2=numpy_array1.reshape(5,2)
print(numpy_array2)

print(numpy_array1.max)
print(numpy_array1.min)
print(numpy_array1.sum())

#satırlar toplamı
print(numpy_array2.sum(axis=1))
#sütunlar toplamı
print(numpy_array2.sum(axis=0))

#mean, medyan, varyans ve standart sapma hesaplamak
print(numpy_array1.mean())
print(numpy_array1.median())
print(numpy_array1.var())
print(numpy_array1.std())



