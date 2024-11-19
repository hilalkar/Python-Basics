import numpy as np

#a=np.array([[1,2,3,4,5]])
# print(a.ndim)
# print(a.shape) # (1,5) bir satır ve bir sütundan oluşur
# print(a)
#
# a=a.squeeze()
# print(a.ndim)
# print(a.shape)
# print(a)

# a=a.reshape((-1,1))
# print(a.ndim)
# print(a.shape)
# print(a)
#
a=np.array([[1,3,5,7,9],[2,4,6,8,10],[1,2,3,4,5]])
# print(a)
# print(a[1:,1:-1])
#
# b=a[[1],:]
# print(b)
# print(b.shape)
#
# c=np.arange(2,7,2)
# print(c)
# print(c.shape)
#
#d=np.random.random((10,2))*8-5
#print(d)
#np.random.random() fonksiyonunu tek başına çalıştırdığınızda da, her seferinde 0 ile 1 arasında farklı bir rastgele sayı dönecektir
#10x2 boyutunda bir dizi oluşturur ve her elemanı [0, 1) aralığında rastgele sayılardan oluşur.
#
# e=np.array([[1,2,3,4,5],[4,5,6,7,8],[1,3,5,7,9]])
# print(e)
# f=np.concatenate((np.zeros((1,e.shape[1])),e,
#                   np.zeros((1,e.shape[1]))),axis=0)
# g=np.concatenate((np.zeros((f.shape[0],1)),f,
#                   np.zeros((f.shape[0],1))),axis=1)
# print(g)
# e.shape[0] satır sayısını e.shape[1] sütun sayısını verir

#
# h=np.array([1,2,3,4])
# j=h.copy()
# j[2]=88
# print(h)
# print(j)
# # np.save('aaa.npy',j)     #Bu satır, j dizisini 'aaa.npy' adında bir dosyaya kaydeder.
# ppp=np.load('aaa.npy')
# print('ppp=',ppp)
# np.save fonksiyonu, NumPy dizilerini .npy formatında kaydeder ve böylece NumPy'nin yerleşik load fonksiyonu ile kolayca tekrar yüklenebilir.