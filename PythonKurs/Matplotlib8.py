import matplotlib.pyplot as plt
# HİSTOGRAM GRAFİĞİ (SÜTUN GRAFİĞİ)

ages = [2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]
range = (0,100)
bins = 10   #bins = 10, histogramda kaç aralık (bin) olacağını belirtir. Burada, 0 ile 100 arasındaki yaşları 10 aralığa böler.
plt.hist(ages,bins,range, color="green", histtype="bar", rwidth="0.8" )
plt.xlabel("age")
plt.ylabel("No.of people")
plt.title(" My Histogram")
plt.show()

