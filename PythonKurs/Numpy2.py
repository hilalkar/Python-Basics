# ndim ile bir dizinin boyutunu öğrenme
import numpy as np
dizi0 = np.array(57)
dizi1 = np.array([2,4,6,8,10])
dizi2 = np.array([[1,3,5,7,9],[2,4,6,8,10]])
dizi3 = np.array([[[1,3,5,7,9], [2,4,6,8,10]]
                  [[1,3,5,7,9], [2,4,6,8,10]]])

print(dizi0.ndim)
print(dizi1.ndim)
print(dizi2.ndim)
print(dizi3.ndim)

print(dizi1[0]*dizi1[1])

