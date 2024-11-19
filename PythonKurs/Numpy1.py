import numpy as np
dizi= np.array(['A','B','C','D'])
print(dizi)
print(type(dizi))

#Numpy ndarray nesnesi oluşturma ve tipini belirleme
import numpy as np
a = np.array([[1,2,3],[4,5,6]],dtype=np.float32)
print (a.ndim, a.shape, a.dtype)  # ndim:boyutu , shape:şekli, dtype:veri türünü verir

#ndarray oluşturmak için list set dict gibi herhangi bir dizi nesnesi array() ile bir ndarray biçiminde dönüştürülüyor
import numpy as np
tuple_dizi = np.array((34,35,57,3))
print(tuple_dizi)

# 1-D bir array oluşturalım
import numpy as np
cift_dizi=np.array([2,4,6,8,10])
print(cift_dizi)

# 2-D bir dizi oluşturalım
import numpy as np
dizi = np.array([[2,4,6,8,10],[1,3,5,7,9]])
print(dizi)

# 3-D bir dizi oluşturalım .üç boyutlu diziler genellikle üçüncü dereceden bir tensörü temsil etmek için kullanılır
import numpy as np
dizi3D = np.array([[[2,4,6,8,10],[1,3,5,7,9]],[[2,4,6,8,10],[1,3,5,7,9]]])
print(dizi3D)