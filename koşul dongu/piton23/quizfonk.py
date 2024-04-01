#Soru 1: Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde doldurun
""""
def ustsel():
    a=int(input("lutfen bir tamsayi giriniz : "))
    b=int(input("lutfen tam sayinin kuvvetini giriniz : "))
    sonuc=a**b
    return sonuc

print(ustsel())

#Soru 2: Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde ve ** yerine for döngüsü ile hesaplayacak bicimde olusturun
def ustsel_dongu(a,b):
    sonuc=1
    if b<1:
        sonuc=1
    else:
        for kuvvet in range(1,b+1):
            sonuc=sonuc*a
        return sonuc
print (ustsel_dongu(3,2))

#Soru 3: Asagidaki fonskiyonu 1 parametre alacak (sadece sayilardan olusan liste tipinde) ve en büyük iki sayiyi döndürecek bicimde olusturun¶
def en_buyuk_dondur(liste):
    liste.sort()
    return liste[-1],liste[-2]
    
    
liste1=[112,2,4,5,6,4,7,98,78,5,7568,876,567,5675,7567,856,76,456,345,756,345,9876]
print(en_buyuk_dondur(liste1))
"""
#Soru 4: Asagidaki fonskiyonu 1 parametre alacak (liste tipinde)
#ve sadece str tipindeki degerleri filter ve lambda ifadelerini kullanarak filtreleyecek bicimde olusturun
""""
def str_tip(liste):
    sonuc =[]
    for tip in liste:
        if  type(tip)==str:
            sonuc.append(tip)
        else:
            pass
    return sonuc

liste=["fdsds","dsdsa","dsaDAS","AS",233,2,3243,2324,4343546,3532,34,"dsfgs"]

#print(str_tip(liste))
def str2(liste):
    
    return [*filter (lambda tip: tip if type(tip) == str else None,liste)]


print(str2(liste))

#Soru 5: Asagidaki fonskiyonu 1 parametre alacak (sadece sayi iceren liste tipinde) ve map ve lambda 
# ifadelerini kullanarak 6 sifir atacak bicimde olusturun¶

def sifir_atici(liste):
    sonuc=[]
    y = 0
    for x in liste:
        if  type(x) != str:
            x = float(x)
            y += 1
            
            x /=1000000
            sonuc.append(x)
        
        else:
            
            print("{0}. elemani olan {1} girdiğiniz değer sayi değldir".format(y, x))
            y += 1
            pass
        
    return sonuc

liste=[10000000,500000,6000000,"a","b",23,"g"]
print(sifir_atici(liste))

def str2(liste):
    return [*map(lambda x: float(x) / 1000000, liste)]
    
liste=[10000000,500000,6000000,23]
print(str2(liste))
"{0} saat , {1} dakika ....".format(saat,dakika)
#Soru 6: Asagidaki fonskiyonu input komutu ile kullanicidan saat ve dakika alacak bicimde olusuturun

def zaman():
    saat=(input("kutfen bir saat belirtiniz : "))
    if saat.isdigit():
        saat=int(saat)
        if 0<=saat<24:
            dakika=input("dakika giriniz: ")
            if dakika.isdigit():
                dakika=int(dakika)
                if 0<=dakika<60:
                    return "Giris yapilan zaman : {0}:{1}".format(saat,dakika)
                else:
                    print("girilen dakika yanlis...")
            else:
                print("girilen dakika yanlis veri tipinde...")
        else:
            print("girilen saat degeri  yanlis aralikta...")        
    else:
        print("girilen saat yanlis veri tipinde...")
                    
    
print(zaman())
"""
