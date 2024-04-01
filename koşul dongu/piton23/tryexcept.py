"""""
def tam_sayi_yuvarlama():
    girdi = input("lütden bir sayi giriniz:  ")
    girdi=float(girdi)
    print ("yuvarlama islemğinin sonucu:  {}".format(round(girdi)))

print(tam_sayi_yuvarlama())

def tam_sayi_yuvarlama2():
    girdi = input("lütden bir sayi giriniz:  ")
    try:
        girdi=float(girdi)
        print ("yuvarlama islemğinin sonucu:  {}".format(girdi))
    except:
        print("{} girdisi yuvarlanmaya uygun bir içerik değidir...".format(girdi))

print(tam_sayi_yuvarlama2())

def tam_sayi_yuvarlama3():
    girdi = input("lütden bir sayi giriniz:  ")
    try:
        girdi=float(girdi)
        
    except:
        print("{} girdisi yuvarlanmaya uygun bir içerik değidir...".format(girdi))
    else:
        print ("yuvarlama islemğinin sonucu:  {}".format(round(girdi)))

print(tam_sayi_yuvarlama3())

def tam_sayi_yuvarlama4():
    girdi = input("lütden bir sayi giriniz:  ")
    status=" "
    try:
        girdi=float(girdi)
        print ("yuvarlama islemğinin sonucu:  {}".format(girdi))
        status="basarili"
    except:
        print("{} girdisi yuvarlanmaya uygun bir içerik değidir...".format(girdi))
        status="basarisiz"
    finally:
        print("tam sayiya cevirme islemi {} olarak tamamlandi...".format(status))

print(tam_sayi_yuvarlama4())

def tam_sayi_dongu():
    while True:
        girdi = input("lütden bir sayi giriniz:  ")
        try:
            girdi=float(girdi)
            print ("yuvarlama islemğinin sonucu:  {}".format(girdi))
            break
        except:
            print("{} girdisi yuvarlanmaya uygun bir içerik değidir...".format(girdi))
            pass

print(tam_sayi_dongu())

try:
    5+"a"
except IndexError :   #burada 5 +a işleminde normalde type error alırım ama type error aldıgım halde ındex error yazarsam tekrar ayhnı ahatayı alırıö
    print("girilen kod blogunda bu tarz bir işlem yapilamaz...")  #bu yuzden asagıda bir tane daha except tanımalandı daha genel oldugu ıcın o devreye girer
except:     # bu işemle hata tiplerine gore kod blogu crash olmıyacak sekilde devam etmesi amaçlanmaktadır...
    print("kod hatali...")    

liste=[]   
try:
    print(liste[-1])
except IndexError:
    print("listede belirtilen indexte eleman yok...")    #burada ilk excepti daralttıgımız hata skalasında olan hata oldugu icin;
except :                                                 #burada ki excepte gecmez 
    print("kod bozuk...")    


vatandas={
    "AD":"MERT" ,
    "TC_NO" : "152444"
}
try:
    print (vatandas["pass_no"])
except KeyError:
    print ("vatandas dictionary icerisinde belirtilen key bulunmamaktadir...")
except:
    print("kod bozuk")   
"""
