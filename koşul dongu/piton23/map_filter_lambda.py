def karesini_(x):
    return x**2
print(karesini_(5))

sayilar=[*range(1,10)]
print(sayilar)
for index in range(len(sayilar)):
    sayilar[index]=karesini_(sayilar[index])
print(sayilar)

print([*map(karesini_,sayilar)])   #map(function, iterable) buradaüstte yaptığımız fonksiyonun map sayesinde sayilar ile ilişkilendirir....
"""""

def cift_sayiari_listele(x):      #
    return x if x%2==0 else None
print(cift_sayiari_listele(3))

print([*map(cift_sayiari_listele,sayilar)])      # eger burada filter kullanmadan fonksiyon ve iterableyi kullanmış olsaydık tek sayıları none şeklinde yazdırırdı..
print([*filter(cift_sayiari_listele,sayilar)] )  #filter(function, iterable) burada da cift sayıların yıne fonksiyonu kullanarak listeyle iliskilendirie....



print([*map(lambda sayi:sayi**2 , sayilar)]) # buradda lambda kullanmanın amacı function kullanmadan functionu onun içersinmde tanımlıyoruz....
print([*filter(lambda x: x if x%2==0 else None ,sayilar)])
"""