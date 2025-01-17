# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 

"""
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir('berf\n' , 10)

"""

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınz.

"""
def listeyeCevir(*args):
    liste = []

    for arg in args:
        liste.append(arg)

    return liste

result = listeyeCevir(10,20,30,'Merhaba')
print(result)

"""

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz.

"""
def asalSayilariBul(sayi1 , sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1 :
            for i in range(2, sayi):
                if (sayi % i == 0) :
                    break
            else:
                print(sayi)

sayi1 = int(input('sayı1 : '))
sayi2  = int(input('sayı2 : '))

asalSayilariBul(sayi1, sayi2)

"""

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür.

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

result = tamBolenleriBul(20)

print(result)