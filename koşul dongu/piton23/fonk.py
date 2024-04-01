"""""
def yazdir():
    print(5)
yazdir()
""" 
"""""
def sayi_dondur(sayi=3242):
    return sayi
print(sayi_dondur(556))
"""
"""""
def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif a<b:
        return b
print(buyuk_sayi_dondur(56,345))


def metin_yazdir(a,b):
    buyuk_sayi=buyuk_sayi_dondur(a,b)
    sablon_metin="{} Daha buyuk sayidir...".format(buyuk_sayi)
    return sablon_metin
print(metin_yazdir(5,10)),
"""
"""""
def isim_soyisim_ayirma(isim_soyisim):
    isim=isim_soyisim.split()[0]
    soyisim=isim_soyisim.split()[1]
# sonuc="ismi: {0} , soyismi: {1} 'dir...".format(isim,soyisim)
    return isim,soyisim
print(isim_soyisim_ayirma("gökçe gün"))
a,b=isim_soyisim_ayirma("mert keskin")
print(a)
print(b)
"""
"""""
# "-".join(["gokce","gun"]) bu komut gokce-gun olarak yazdırılmasını saglıyor yanı ne koyarsam onunla bırlestırrır.
def isim_soyisim_birlestirme(isim,soyisim):
    return "   taha   ".join([isim,soyisim])
print(isim_soyisim_birlestirme("mert","keskin"))
"""
"""""
def isim_soyisim_birlestirme2(*args): #buradaki args liste gibi dusunebirlirsin mainde kactane deger icerisine yazarsan yaz dondurebilirsin....
    for item in args:
        print(item)
    return " ".join(args)
print(isim_soyisim_birlestirme2("mert","keskin","taha"))
"""
"""""
def gobek_adi_yazdir(**kwargs):    #buradaki **kwargs argümanı girdigin içerikleri bir dictionary e atar ve buradan işlemlerini yaparsın....
    if "gobekadi" in kwargs:
        print(kwargs.get("gobekadi"))
    else:
        print("gobek adi yok...")
print(gobek_adi_yazdir(isim="mert",soyismi="keskin",gobekadi=l"doberman"))
"""
    
    
