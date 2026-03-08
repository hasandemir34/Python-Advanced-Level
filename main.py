print("*"* 60)
print(("SECTİON 1  DECORATORS"))
print("*"* 60)



def my_decorator(func):
    def wrapper():
        print("--- Fonksiyon çalışmadan ÖNCEKİ hazırlıklar ---")
        func()  # Asıl fonksiyon burada çağrılıyor
        print("--- Fonksiyon çalıştıktan SONRAKİ işlemler ---")
    return wrapper

def say_hello():
    print("Merhaba Dünya!")

@my_decorator #bunun sayesinde oto olarak decorator old. belirtmiş oluyorum.
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