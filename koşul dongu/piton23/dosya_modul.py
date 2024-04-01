import os

print(os.getcwd())
print(os.listdir("C:\\Users"))
#bu komut suan bulunan konumu istedigim yere atamamı saglıyor

print(os.listdir())     

dosyalar=os.listdir()
for eleman in dosyalar:
    print(eleman + "mertt")

#os.mkdir("C:\\Users\\tahak\\Desktop\\piton\\piton23")   bu kod piton 23 klasorunu eklememızı sagladı

print(os.listdir())   
"""""

yeni_dosya=os.open("yeni_dosya.txt0",os.O_RDWR|os.O_CREAT)
os.write(yeni_dosya,"merhaba dünya".encode())           #burda klasorun icerisine yeni text dosyasi olusturduk ve icerisine ne yazcagimizi gosterdik
                                                        #encode buradqa str tipi deiskeni byte cinsine cevirerek texte yazilmasini olanakli kilar.
os.close(yeni_dosya)
"""
yeni_dosya=os.open("yeni_dosya.txt0",os.O_RDONLY)
istatistik=os.stat(yeni_dosya).st_size
icerik= os.read(yeni_dosya,13)                           #burda da secili dosyanin icerisini okumasi icin komut veridk ne kadar uzunlukta okumasini belirttik
print(icerik.decode)                                               #decode komut encode komutunun tersi olarak calismaktadir yani byte indirgenen eski haline doner
print(istatistik)                                      #os.stat komutu text dosayasi hakkinda tum bilgilere ulasamamızı saglar icersinde ne kadar karakter barindigini gorebiliriiz
os.close(yeni_dosya)
os.unlink("yeni_dosya.txt0")                                #olusturdugumuz dosayayi silmek icin kullandigimiz komuttt...
