"""""
class Ucus():
    havayolu="THY"
    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu) :
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu
    def __repr__(self) :
            return "{} sefer sayili {}--{} ucusumuz {} dakika surecektir".format(
            self.kod ,
            self.kalkis,
            self.varis,
            self.sure
        )
    def anons_yap(self):
        return "{} sefer sayili {}--{} ucusumuz {} dakika surecektir".format(
            self.kod ,
            self.kalkis,
            self.varis,
            self.sure
        )
    def koltuk_sayisi(self):
        return self.kapasite-self.yolcu
    def bilet_satis(self, bilet_adedi=1):
        if self.koltuk_sayisi() >= bilet_adedi:
            self.yolcu += bilet_adedi
            print("{} adet bilet satilmiştir. Kalan koltuk sayisi: {}".format(
                bilet_adedi, self.koltuk_sayisi()))
        else:
            print("Yetersiz koltuk sayisi. Daha az bilet satin alin.")
    def bilet_iptal(self, bilet_adedi=1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            print("{} adet bilet iptal edilmistir. Kalan koltuk sayisi: {}".format(
                bilet_adedi, self.koltuk_sayisi()))
        else:
            print("Yetersiz yolcu sayisi. Daha az bilet iptal edin.")
ucus1=Ucus("TK123","İST","ANK",50,300,65)
ucus2=Ucus("TK1233","ANT","ANK",40,850,95)

print(ucus1.anons_yap())
ucus1.bilet_satis(5)
ucus1.bilet_satis(5)
print(ucus2.anons_yap())
ucus2.bilet_iptal(20)
#print(ucus1.__dir__())
print(ucus1)            # bu satirda ki kod normalde ucusun memoryde tutuldugu yeri gosterir 
#                        ancak __repr__ adli ozellik sayesinde bunu anlayacagımız sekılde gosterebi
"""
class Seyehat():
    def __init__(self,kalkis,varis) :
        self.kalkis=kalkis
        self.varis=varis
    def anons(self):
        return "{}--{} seyehatine hosgeldiniz".format(self.kalkis,self.varis)
class otobus(Seyehat):
    def __init__(self,mola_duraklari,kalkis,varis):
        Seyehat.__init__(self,kalkis,varis)
        self.mola_duraklari=mola_duraklari
        
seyehat1=Seyehat("ANT","BOD")
print(seyehat1.anons())
oto1=otobus(["FET","ALN"],"ANT","BOD")
print(oto1.mola_duraklari)


