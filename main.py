
# 21-m
class Internet:
    def __init__(self, egasi, mb):
        self.egasi = egasi
        self.__mb = mb

    def qosh(self, mb):
        self.__mb += mb

    def ishlat(self, mb):
        self.__mb -= mb

    def info(self):
        print(f"Egasi: {self.egasi}")
        print(f"Qolgan MB: {self.__mb}")


i1 = Internet("Ali", 1000)
i1.info()

i1.ishlat(200)
i1.info()

i1.qosh(500)
i1.info()


# 22-m
class Restoran:
    def __init__(self, nomi, mijozlar):
        self.nomi = nomi
        self.__mijozlar = mijozlar

    def kelish(self, n):
        self.__mijozlar += n

    def ketish(self, n):
        self.__mijozlar -= n

    def info(self):
        print(f"Restoran: {self.nomi}")
        print(f"Mijozlar: {self.__mijozlar}")


r1 = Restoran("Osh Markazi", 50)
r1.info()

r1.kelish(20)
r1.info()

r1.ketish(10)
r1.info()
