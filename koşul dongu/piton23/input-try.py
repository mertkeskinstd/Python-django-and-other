"""""
def uygulama():
    girdi=int(input("kütfen bir sayi giriniz: "))
    islem=str(input("verinin tek mi cift mi olduğunu sorgula: "))
    if islem=="cift":
        if girdi%2==0:
            return "evet {0} sayisi cift bir sayidir...".format(girdi)
        else:
            return "hayir {0} sayisi cift bir sayi degildir...".format(girdi)
    elif islem=="tek":
        if girdi%2==0:
            return "evet {0} sayisi tek bir sayidir...".format(girdi)
        else:
            return "hayir {0} sayisi tek bir sayi degildir...".format(girdi)

print(uygulama())
"""
"""""
def sayi_girdi_kont() :
    girdi=input("lutfen bir sayi girniz: ")
    if girdi.isdigit():
        print("tebrikler integr bir deger girdiniz...")
    else :
        print("üzgünüm integr tipi degisken girmediniz...")

print(sayi_girdi_kont())
"""
"""""
def sayi_girdi_dongu():
    girdi=input("lutfen bir sayi girniz: ")
    while not girdi.isdigit():
        print("malesef {0} variablesi integer bir variable degildir tekrar deneyiniz...".format(girdi))
        girdi=input("lutfen bir sayi girniz: ")
    else:
        print("tebrikler integr bir deger girdiniz...")

print(sayi_girdi_dongu())
"""
"""""
def eposta_kont():
    girdi=input("lutfen gecerli bir eposta adresi giriniz: ")
    while not (("@" in girdi )  and  ("." in girdi )    ):
        print("üzgünüm {0} eposta adresi degildir...".format(girdi))
        girdi=input("lutfen gecerli bir eposta adresi giriniz: ")
    else:
        print("tebrikler {} adresi gecrlidir...".format(girdi))    

print(eposta_kont())
"""      

def faktor():
    x=int(input("lutfen bir sayi giriniz: "))
    sayi=1
    while x+1>1:  
        sayi *= x
        x -=1
    sonuc=sayi
    return sonuc

print(faktor())




