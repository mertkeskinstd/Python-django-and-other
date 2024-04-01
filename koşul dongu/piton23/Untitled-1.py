#havadurumu="karli"
#if havadurumu=="yagisli":
#   print("semsiyeni al")
#if havadurumu=="yagisli":
# print("semsiyeni al")
#else:
# print("sorun yok")
#if havadurumu=="yagmurli":
#    print("semsiyeni al")
#elif havadurumu=="karli":
#   print("atkini al")
#else:
#   print("sorun yok")
#liste=["a","b","c"]
#hedef_harf="b"
#if (hedef_harf in liste) and (hedef_harf == liste[0]) :
#   print("sorun  yok")
#elif (hedef_harf in liste) :
#   print("ilkdeil")
#else:
#    liste.append(hedef_harf)
#    print("güncel liste{}".format(liste))

#sayilar = [1,3,5,7,9,12,19,21]

#hangi sayılar 3 ün katıdır.
"""
for sayi in sayilar:
    if(sayi%3==0):
        print(sayi)
"""
#sayılar lıstesınde sayıların toplamı kaçtır
"""""
toplam=0
for sayi in sayilar:
    toplam+=sayi    
print("sayilarin toplami: {0}".format(toplam))
"""
#sayilar listesindeki tek sayilarin karesinş aliniz
"""""
for sayi in sayilar:
    if(sayi%2==1):
        print(sayi**2)
"""
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
#sehirlerden hangileri en fazla 5 karakterlidir
"""""
for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir)
"""

urunler = [
{'name':'samsung S6', 'price': '3000' },
{'name':'samsung S7', 'price': '4000' },
{'name':'samsung S8', 'price': '5000' },
{'name':'samsung S9', 'price': '6000' },
{'name':'samsung S10', 'price': '7000' }
]
#urunlerin toplamının fiyatı nedir
"""""
toplam=0
for x in urunler:
    fiyat = int(x.get('price'))  #int(x['price']) 
    toplam +=fiyat
print(toplam)

#urunlerin fiyatı en az 5000 olan urunleri gosterınız
for x in urunler:
    fiyat=int(x.get("price"))
    if(fiyat>=5000):
        print(fiyat)
"""

"""
moderator="ferhat iibrik"
kullanici_sayisi=0
moderator_sayisi=0
yorum_birakanlar=["ismail aydemir","uygar aydin","naz yagicioglu","ferhat iibrik","ulas acil","bilal  kurucay"]
for kullanici in yorum_birakanlar:
    ad= kullanici.split()[0]
    soyad= kullanici.split()[1]
    if(moderator==kullanici):
        moderator_sayisi +=1
        print("{0}. moderatorun adi: {1} ve soyadi: {2}".format(moderator_sayisi,ad,soyad) )
    else:
        kullanici_sayisi=kullanici_sayisi+1
        print("{0}. kullanicinin adi: {1} ve soyadi: {2}".format(kullanici_sayisi,ad,soyad) )
"""



#for x in yorum_birakanlar:
#    kullanici_sayisi=kullanici_sayisi+1
#    ad= x.split()[0]
#    soyad= x.split()[1]
#    print("{0}. kullanicinin adi: {1} ve soyadi: {2}".format(kullanici_sayisi,ad,soyad) )
"""""
tup1=(1,3,5,7)

for sayi in tup1:
    print(sayi)
"""
"""""
liste=[[1,2],[3,4],[5,6]]

for x,y in liste:
    print(x*y)
"""  
dict1={
    "ad" : "naz" ,
    "soyad" : 'yagcioglu'
}
print(dict1.items())    

for k , v in dict1.items():
    print("key :{0}\t values : {1}".format(k,v))

for k in dict1.keys():
    print("keys: {0}".format(k))