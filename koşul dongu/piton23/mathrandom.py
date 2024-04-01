import random
import math
"""""
#print(random.__dir__())
#help(random)
print(random.random())              #random komutu 0 ve 1 arasinda bir deger sallar...
print(random.uniform(5,10))         #burdada goruldugu uzere 5 ve 10 arasinda sayi salladi...
print(random.randint(4,9))          #burdada rastgele bir tam sayi olusturabiliyoruz
a=[*range(1,50)]
print(a)
print(random.choice(a))             #burda range ile olusturdugumuz liste icerisinden choice komutu ile rasgele bir sayi sectik

print(random.sample(a,k=4))         #burada sample komutu icerisinde kactane rasgele deger istedigimizi k ile belirtiyoruz
random.shuffle(a)                   #burada shuffle komutu belirli bir listeyi karistirmaya yarar....
print(a)                    
"""
print(round(8.8))                   #buradaki round komutu math kutuphanesi icerisinde deildir...
print(math.ceil(7.4))               #burada ceil komutu sayi hep bir sonraki tam sayiya yuvarlar...
print(math.floor(7.8))              #floor komutu ise bir önceki tam sayiya yuvarlar...
print(math.factorial(4))
print(math.pow(3,3))




        