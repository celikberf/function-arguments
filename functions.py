def sayHello(name = 'user') :
   return 'Hello ' + name # yazacagımız kodlar sayHellonun üyesi olcak

msg = sayHello('berf')

print(msg)


def total(numm1, num2):
   return numm1 + num2

result = total(10,20)
result = total(20,30)
print(result)

def yasHesapla(dogummYili):
   return 2024 - dogummYili

ageBerf = yasHesapla(1999)
ageGuler = yasHesapla(1973)
ageSoner = yasHesapla(1991)

print(ageBerf, ageGuler , ageSoner)

def emekliligeKacYilKaldi(dogumyili , isim):
   
   """
   DOCSTRING : Dogum yiliniza goree emekliliginize kaç yil kaldi
   INPUT : Doğum yılı
   OUTPUT : Hesaplanan yıl bilgisi
   
   """
   yas = yasHesapla(dogumyili)
   emeklilik = 65 - yas

   if emeklilik > 0 :
      print(f'emekliliğinize {emeklilik} yıl kaldı')
   else:
      print('Zaten emeklisiniz.')

emekliligeKacYilKaldi(1999, 'berf')

print(help(emekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))