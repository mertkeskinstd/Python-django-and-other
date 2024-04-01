"""""
class Hayvan:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
        def __repr__(self):
            return "{} ismi hayvanin yasi : {}".format(
                self.isim,
            self.yas
            )
    def beslen(self):
        print(f"{self.isim} besleniyor.")
class Kus(Hayvan):
    
    def  __init__(self, isim, yas,tur):
        super().__init__(isim, yas)
        self.tur=tur
    def uc(self):
        print(f"{self.isim} ucuyor")

class Kopek(Hayvan):
    def __init__(self, isim, yas,cins):
        super().__init__(isim, yas)
        self.cins=cins
    def __repr__(self):
            return "{} ismi hayvanin yasi : {}".format(
                self.isim,
            self.yas
            )
    def havla(self):
        print(f"{self.isim} havliyor")

marti=Kus("marti","3","sahin")
kopke=Kopek("reddo","2","pug")

print(marti.uc())
print(kopke.havla())
print(kopke)
print(kopke.beslen())
"""
class Urun:
    def __init__(self,urun_adi,fiyat) :
        self.urun_adi=urun_adi
        self.fiyat=fiyat
    def __str__(self) :
        return  f"{self.urun_adi }  -  {self.fiyat } tl "
class Kullanici:
    def __init__(self,ad,soyad,email) :
        self.ad=ad
        self.soyad=soyad
        self.email=email
        self.satin_alinan_urunler=[]
    def urun_satin_al(self,Urun):
        self.satin_alinan_urunler.append(Urun)
    def toplam_harcama(self):
        toplam=sum(urun.fiyat for urun in self.satin_alinan_urunler)
        return "{} {} toplam {} tl harcadi".format(self.ad,
                                                self.soyad,
                                                toplam)
urun1 = Urun("Laptop", 5000)
urun2 = Urun("Akilli Telefon", 2000)
urun3 = Urun("Televizyon", 3000)
kullanici1 = Kullanici("Ahmet", "Yilmaz", "ahmet@example.com")
kullanici2 = Kullanici("Ayşe", "Demir", "ayse@example.com")

kullanici1.urun_satin_al(urun1)
kullanici1.urun_satin_al(urun2)            
print(kullanici1.toplam_harcama())