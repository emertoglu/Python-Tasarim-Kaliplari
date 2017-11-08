class Yayımcı(object):
    kisiler = set()

    def kaydet(self, kisi):
        self.kisiler.add(kisi)

    def sil(self, kisi):
        self.kisiler.discard(kisi)

    def bildirimGonder(self, mesaj):
        for kisi in self.kisiler:
            kisi.notify(mesaj)


class Abone(object):

    def __init__(self, kisiAdi):
        self.kisiadi = kisiAdi

    def haberVer(self, mesaj):
        print(self.kisiadi + ' alınan mesaj: ' + mesaj)

yayımcı = Yayımcı()

# Create observers that will receive notifications
ali = Abone('Ali')
ahmet = Abone('Ahmet')
yayımcı.kaydet(ali)
yayımcı.kaydet(ahmet)

# Notifications are sent to every observer (subscriber)
yayımcı.bildirimGonder('We updated the website')
yayımcı.bildirimGonder('Make sure to add a profile picture')
