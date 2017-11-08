from random import randrange


class Silah(object):
    isim = None
    maliyet = None

    @staticmethod
    def silah_al(x):
        if x == 0:
            return Bicak()
        if x == 1:
            return Tabanca()


class Bicak(Silah):
    isim = 'Bicak'
    maliyet = 20.000


class Tabanca(Silah):
    isim = 'Tabanca'
    maliyet = 300.000


# Create 25 random weapons
for _ in range(25):
    w = Silah.silah_al(randrange(2))
    print(w.isim, w.maliyet)
