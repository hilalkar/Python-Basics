"""
Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız
1.bakım --> 1.yıl
2.bakım --> 2.yıl
3.bakım --> 3.yıl
4.bakım -->4.yıl

süre hesabını alınan gün,ay,yıl bilgisine göre gün bazlı hesaplayın
datetime modülünü kullanın
simdi-(2018/8/1) = gün

"""
import datetime

tarih = input("Aracınız hangi tarihte trafiğe çıktı (2019/8/9) ?")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark= simdi-trafigeCikis
days = fark.days

if days<=365:
    print("1. servis aralığı")
elif days>365 and days<=365*2:
    print("2.servis aralığı ")
elif days>365*2 and days<=365*3:
    print("3.servis aralığı ")
elif days>365*3 and days<=365*4:
    print("4.servis aralığı ")
else:
    print("hatalı süre girdiniz ")