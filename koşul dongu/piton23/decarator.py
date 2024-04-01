"""""
def deneme():
    print("abc")
f=deneme()
print(f)

def deneme():
    print("deneme fonksiyonu calisiyor")
    def test():
        return "test fonksiyonu calisiyor"  
    print(test())

print(deneme())

def deneme():
    print("deneme fonksiyonu calisiyor")
    def test():
        return "test fonksiyonu calisiyor"  
    return test
f=deneme()
print(f()  )               #burada print(deneme()) bu sekilde dondurdugumuz zaman testi dondurur ama işcindekini ekrana yazmaz buyuzden su sekilde yapabilirz

def deneme():
    return "deneme fonk calisiyor"          #bir fonksiyonu baska bir fonksiyon icinde tanimlamak mumkun...
def ikinci(f):
    print("ikinci fonksiyon calisiyor")
    print(f)

ikinci(deneme())
"""

def deco(f):

    def wrapper():
        print("baslangic")
        f()
        print("bitis")
    return wrapper
"""""
def yazdir():
    print("yazdir")

yazdir=deco(yazdir)                 #bu sekilde yazmaktansa su sekilde yapabilirz...
yazdir()
"""  
@deco
def yazdir():
    print("yazdir")

yazdir()
