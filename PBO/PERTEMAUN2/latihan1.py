# membuat class
class Mobil:
    #membuat class variable
    jumlah_mobil = 0
    #membuat construktor
    def __init__(self, ban, merk, cc):
        #instance variable 
        self.merkban = ban
        self.merkmobil = merk
        self.kapasitas = cc
        Mobil.jumlah_mobil += 1
    #membuat method stringe
    def __str__(self):
        return f"{self.merkban}, {self.merkmobil}, {self.kapasitas}"
    #membuat method baru bore up
    def boreup(self, bore):
        self.kapasitas += bore
#membuat objek baru M1
M1 = Mobil("Bridgestone","toyota-Kijang", 1500)
print(M1)
M1.boreup(500)
print(M1)
#membuat objek baru M2
M2=Mobil("Pirelli", "subaru", 2000)
print(M2)
print("Jumlah Mobil", Mobil.jumlah_mobil)