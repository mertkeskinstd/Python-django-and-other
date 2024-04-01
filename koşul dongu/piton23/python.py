dict1={
    "isim" : "Mesut" ,
    "yas" : 32 ,
    "lokasyon" :{
        "dogdugu_sehir":"Muş",
        "yasadigi_sehir" :"berlin"
    }
}
print(dict1)
print(dict1["yas"])
print(dict1.get("yas"))#üstteki kullanım oldugu gibi get komutu ilede yazdırma sansımız vardır
print(dict1["lokasyon"]["yasadigi_sehir"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())





#liste=["a","b","c","d","e","a"]
#print(liste)
#tup=("a","b","c","d","e","a")
#print(tup)
#liste[0]=4848
#print(liste)
#print(tup.count("a"))   #a dan kactane oldugunu soyler
#print(tup.index(  "b")) #b nin kaçıncı eleman oldugunu soyler
#listedeki 0.elemanımı deıstırebılıyorken tup dakı 0. 
# degeri degistiremem içeresine girilen ddeger kitlenir.
#liste=liste +["f"]
##[:3]baştan listenin ucuncu elemanına kadar demek
##[3:5:2]3. elemandan 5 e kadar bir eleman atlayarak ekrana yazdırmak demek
##sort komutu listelerdeki sayıları sıralamaya yarar yada alfabtik
##reverse komutu listeyi tersten yazar
##pop komutuu listeden belirtilen elemanı cıkaartır
##apppend komutu listeye istenilen elemanı ekler 
#print(liste[3:5])
#liste.append("g")
#print(liste)
#liste.pop(5)
#print(liste)
#sayilar=[546564,54564,546546,6456456,2,2,1,1,3,3]
#print(set(sayilar))
##listenin içerisinde tekrar eden sayılardan var ise onu
#tekrar ettirmeden yazar
##sayilar.sort()
##print(sayilar)
##sayilar.reverse()
#print(sayilar)

