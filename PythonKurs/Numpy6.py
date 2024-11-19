import numpy as np

# ASTYPE() ile veri dönüşümü

arr = np.array([1.1 ,2.1 ,3.1])
newarr = arr.astype(int)
print(newarr)        # [1,2,3]
print(newarr.dtype)  #int64

arr2 = np.array([1,0,3])
newarr2 = arr2.astype(bool)
print(newarr2)
print(newarr.dtype)

# Boyutlandırma shaping
a =np.array([1,2,3,4,5,6])
a =a.reshape(3,2)
a =a.reshape(2,-1) #sekl için -1 ekledik

print(a)
