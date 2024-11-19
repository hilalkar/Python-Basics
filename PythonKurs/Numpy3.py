# 2-D dizi elemanlarına erişim

import numpy as np
dizi = np.array([[1,3,5,7,9],[2,4,6,8,10]])
print(dizi[0,0]) # 1.dizinin ilk elemanı
print(dizi[1,4]) # 2.dizinin 5.elemanı
print(dizi[0,2]) # 1.dizinin 3. elemanı
print(dizi[1,3]*dizi[0,2]) # 2.dizinin 4. ve 1. dizinin 3. elemanının çarpımı


# 3-D dizi elemanlarına erişim
dizi3D = ([[[1,3,5,7,9], [2,4,6,8,10]],
            [[11,13,15,17,19],[12,14,16,18,20]]])

print(dizi3D[0, 1, 2]) # dizinin ilk katmanındaki ikinci diziyi üçüncü elemanı döndürür
