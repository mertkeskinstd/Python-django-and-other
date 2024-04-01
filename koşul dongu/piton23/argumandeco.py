"""""
def deco(f):

    def wrapper(*args):
        print("baslangic")
        f(*args)
        print("bitis")
    return wrapper

@deco
def toplama(a,b):
    print(a+b)
    
toplama(4,5)

def deco(msg1,msg2):
    def ara_katman(f):
        def wrapper(*args):
            print(msg1)
            f(*args)
            print(msg2)
        return wrapper
    return ara_katman

@deco("ilk","sonuc")
def toplama(a,b):
    print(a+b)

toplama(4,5)
"""
#sure polcumlemesi
import time


def sure_olc(f):
    def wrapper(*args):
        baslangic=time.time()
        print(f"baslangic zamani:\t {baslangic}")
        
        f(*args)
        bitis=time.time()
        print(f"bitis zamani:\t {bitis}")
        print(f"gecen zaman:\t {bitis-baslangic}")
    return wrapper

@sure_olc
def faktoriyel(sayi):
    
    sayac=1
    while 1<sayi:
        sayac=sayi*sayac
        sayi -=1
    print(sayac)

faktoriyel(1000)

    
    
