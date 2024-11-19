import numpy as np
#numpy dizilerde arama where() yöntemini kullanırız

arr=np.arr(1,2,3,4,5,4,4)
x = np.where(arr==4)
print(x)  #array[3,5,6]


arr1=np.array([1,2,3,4,5,6,7,8])
x2 = np.where(arr1%2==0)
print(x2) #array[1,3,5,7]
