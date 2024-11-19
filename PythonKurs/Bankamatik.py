from turtledemo.sorting_animate import enable_keys

hesapA = {
    "ad": "Sadık Turan",
    "hesapNo": "13245678",
    "bakiye": 3000,
    "ekHesap":2000
}
hesapB= {
    "ad": "Hilal Kar",
    "hesapNo": "12345678",
    "bakiye": 5000,
    "ekHesap":1000
}
hesapC = {
    "ad": "Emel Ay",
    "hesapNo": "12345678",
    "bakiye": 1000,
    "ekHesap":500
}
def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print("Paranızı çekebilirsiniz")
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam>=miktar):
            ekHesapKullanimi = input("ek hesap kullanılsın mı (e/h)")
            if ekHesapKullanimi=="e":
                ekHesapKullanilacakMiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("üzgünüz bakiye yetersiz")


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} lu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır  ")

paraCek(hesapB,8000)
bakiyeSorgula(hesapC)


