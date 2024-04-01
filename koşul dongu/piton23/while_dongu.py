"""""
x=0
while(x<10):
    print("{}' degeri 10'dan kucuktur.".format(x))
    x +=1

sayi=6
sonuc=1
while (sayi>0):
    sonuc=sonuc*sayi
    sayi -=1
print(sonuc)
"""
#range kullanımı...
"""""
print(list(range(10)))
print([*range(10)])
print([*range(2,7,2)])

for sayi in range(10):
    print(sayi)
"""
#enumerate kullanımıı...
"""""
harfler=["a","b","c","d","e"]
for ,harf in enumerate(harfler):
    print(harf)

harfler=["a","b","c","d","e"]
for index,harf in enumerate(harfler):
    print(" {0}. harf: {1}".format(index+1,harf))
    """ 
#for içerisindeiki tane değişken aıarak yapıcagımz ıslemı zıp aynı uzunluga sahıp lıstelerde yapabılıyor
"""""
ulkeler=["TR","FR","EN"]
siralama=range(1,4)
for birles in zip(ulkeler,siralama):
    print(birles)
"""
#break komutuu kullanımı...
"""""
harfler=["a","b","c","d","e"]*100
for index,harf in enumerate(harfler):
    if harf=="c":
        print("{} harfi şu indexte tutuluyor: {}".format(harf,index) )
        break
"""  
#contiune komutu kullanımı...
"""""
for sayi in range(1,6):
    if sayi%2==0:
        continue
    print(sayi)
"""
#pass komutu kullanımı...
"""""
for sayi in range(1,6):
    if sayi%2==0:
        pass
    else:
        
        print(sayi)
"""  
"""""
metin = "Python programlama              dili"
bosluk_sayisi = 0

for karakter in metin:
    if karakter == ' ':
        bosluk_sayisi += 1

print("Boşluk sayisi:", bosluk_sayisi)
"""
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = []

for sayi in sayilar:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)

print("Çift sayilar:", cift_sayilar)









