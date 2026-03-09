print("*"* 60)
print(("SECTİON 1  DECORATORS"))
print("*"* 60)



def my_decorator(func):
    def wrapper():
        print("--- Fonksiyon çalışmadan ÖNCEKİ hazırlıklar ---")
        func()  # Asıl fonksiyon burada çağrılıyor
        print("--- Fonksiyon çalıştıktan SONRAKİ işlemler ---")
    return wrapper



@my_decorator #bunun sayesinde oto olarak decorator old. belirtmiş oluyorum. genelde çalışma zamanında kullanılır ölçmek için
def say_hello():
    print("Merhaba Dünya!")

say_hello()



def decora(func):
    def wrapper():
        print("////"*20)
        func()
        print("işlem bitti üstad")
    return wrapper

@decora
def saysa():
    print("herkese kolay gelisn")

saysa()


print("*"* 60)
print(("SECTİON 2 PROPERTY DECORATORS"))
print("*"* 60)

class Ogrenci:  #private ya da encapsulation hakkında bi konu
    def __init__(self, notu):
        self._notu = notu # '_' işareti "private" (özel) olduğunu temsil eder.


    # GETTER: Değeri okumak istediğimizde çalışır
    @property
    def notu(self):
        #print("Not okunuyor...")
        return self._notu

    # SETTER: Değeri değiştirmek istediğimizde çalışır
    @notu.setter
    def notu(self, yeni_not):
        if 0 <= yeni_not <= 100:
            print(f"Not {yeni_not} olarak güncellendi.")
            self._notu = yeni_not
        else:
            print("Hata: Not 0 ile 100 arasında olmalı!")

# --- KULLANIM ---
hasan = Ogrenci(85)

print(hasan.notu)   # Arka planda @property (getter) çalışır.
hasan.notu=99
print(hasan.notu)




print("*"* 60)
print(("SECTİON 3 statik method"))
print("*"* 60)


class matskütüp():

    @staticmethod
    def add(x,y):
        return x+y


print(matskütüp.add(5,20))

#farklı bir statik örneği
class Validator:

    @staticmethod
    def is_valid_email(email):
        # Basit bir kontrol: İçinde '@' var mı?
        return "@" in email and "." in email

    @staticmethod
    def is_valid_age(age):
        # Yaş 0 ile 120 arasında mı?
        return 0 <= age <= 120

#deneme örnekleri oluşturduk hemen
user_email = "hasan@example.com"
user_age = 70

if Validator.is_valid_email(user_email) and Validator.is_valid_age(user_age):
    print("Veriler geçerli, kayıt yapılabilir.")
else:
    print("Hatalı veri girişi!")

print("*"* 60)
print(("SECTİON 4 class method"))
print("*"* 60)


class Pizza:
    # Sınıf değişkeni (Tüm pizzalar için ortak veri)
    total_pizzas = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        # Her yeni pizza oluşturulduğunda sayacı 1 artırıyoruz
        Pizza.total_pizzas += 1

    @classmethod
    def margherita(cls):
        # cls() demek aslında Pizza() demek.
        # Burada "Peynir, domates, fesleğenli bir Pizza yap" diyoruz.
        return cls(["peynir", "domates", "fesleğen"])

    @classmethod
    def pepperoni(cls):
        # Burada "Peynir, sucuk, domatesli bir Pizza yap" diyoruz.
        return cls(["peynir", "sucuk", "domates"])

    @classmethod
    def get_total_pizzas(cls):
        # Sınıfın üzerindeki toplam pizza sayısını döndürür
        return cls.total_pizzas

# --- KULLANIM ---

# 1. Margarita siparişi (Class method ile nesne üretme)
pizza1 = Pizza.margherita()
print(f"Pizza 1 Malzemeleri: {pizza1.ingredients}")

# 2. Pepperoni siparişi
pizza2 = Pizza.pepperoni()
print(f"Pizza 2 Malzemeleri: {pizza2.ingredients}")

# 3. Toplam kaç pizza yapıldığını sorgulama
print(f"Toplam Satılan Pizza Sayısı: {Pizza.get_total_pizzas()}")



print("*"* 60)
print(("SECTİON 5 abstract method"))
print("*"* 60)

from abc import ABC, abstractmethod

class Animals(ABC):

    
























