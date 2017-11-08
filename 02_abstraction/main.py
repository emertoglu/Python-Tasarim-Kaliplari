class Dikdortgen(object):

    @staticmethod
    def alan_hesapla(genislik, uzunluk):
        return genislik * uzunluk



# Kullanıcı dikdörtgen alanını  bulmak için formülü(Sınıfın yapısını) bilmek zorunda değildir
alan=Dikdortgen.alan_hesapla(7,8)
print(alan)
