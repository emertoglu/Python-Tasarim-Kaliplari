class Enemy(object):

    def sola_don(self):
        print("Sola dönüldü")

    def saga_don(self):
        print("Saga dönüldü")


class Ninja(Enemy):

    def karete_yap(self):
        print("karete yapıldı")


class Zombie(Enemy):
    def isir(self):
        print("O'nu ısırdı")


enemy=Enemy()
enemy.sola_don()
enemy.saga_don()

# Ninja aynı zamanda üst sınıfın tüm işlevlerini içerir (Enemy)
ninja=Ninja()
ninja.karete_yap()
ninja.sola_don()
ninja.saga_don()

#Zombie sınıfı üst sınıfın tüm işlevlerini yapar (Enemy)
zombie=Zombie()
zombie.isir()
zombie.sola_don()
zombie.saga_don()
