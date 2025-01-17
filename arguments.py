def changeName(n):
    n = 'berf'

name = 'guler'

changeName(name)
print(name) 

# referans kodlaması yapıyoruz. guler ile değiştirdik  aşağıda da istanbul olarak değiştirdik.

def change(n):
    n[0] = 'istanbul'

sehirler = ['ankara ' , 'izmir']

change(sehirler[:]) # burdakı iki nokta ile kopyasını aldık birrebir aynı

print(sehirler)
"""
def add(a, b, c = 0 ): #3. parametreyi kullanıp kullanmayacagımı bilmiyorum
    return sum ((a,b,c)) # pyhton kütüphanesi ile geliyo. Bir fonksiyon . list fonksiyonu gibi 

print(add(10,20))
print(add(10,20,30)) # en az 2 en fazla 6 parametre gönderebiliriz.
"""
"""

def add(*params): # istediğimiz kadar parametre gönderebilirz.
    sum = 0
    for n in params : 
        sum = sum + n
    return sum


print(add(10,20,50))
print(add(10,20,30))
print(add(10,20,30,40)) 
"""

def displayUser(**args): # bir dictionary gelcek o yüzden ** koydk
    print(type(args))
    for key,value in args.items():
        print('{} is {}'.format(key,value))


displayUser(name = 'Berfin', age = 25, city = 'Ankara')
displayUser(name = 'Güler', age = 52, city = 'Ankara' , phone = '9299292')
displayUser(name = 'Soner', age = 33, city = 'Ankara', phone = '292929210', email = 'soner@gmail.com')

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10, 20 , 30 , 40 , 50 , key1 = 'value 1 ' , key2 = 'value 2')