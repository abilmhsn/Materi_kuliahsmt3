class buku:
    def __init__(self, judul, penulis, tahun_terbit): 
        self.namajudul = judul
        self.namapenulis = penulis
        self.tahun_terbit = tahun_terbit

    def __str__(self):
        return f"{self.namajudul}, {self.namapenulis}, {self.tahun_terbit}"
    
    def boreup(self, tahun):
        self.tahun_terbit = tahun

B1 = buku("Dunia shoope","joestin gaarder", 1991)
print(B1)
B1.boreup(1991)
print(B1)

B2 = buku("filosofi teras", "Henry Menampiring", 2018)
print(B2)
B2.boreup(2018)
print(B2)



