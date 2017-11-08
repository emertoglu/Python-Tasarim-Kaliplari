class Bas(object):

    def __init__(self, goz_rengi, sac_rengi):
        self.goz_rengi = goz_rengi
        self.sac_rengi = sac_rengi


class Govde(object):

    def __init__(self, boy):
        self.boy = boy


class Kisi(object):

    def __init__(self, goz_rengi, sac_rengi, boy):
        self.bas = Bas(goz_rengi, sac_rengi)
        self.govde = Govde(boy)

    def print_goz_rengi(self):
        print(self.bas.goz_rengi)

ahmet = Kisi('mavi', 'sarisin', 170)
ahmet.print_goz_rengi()
