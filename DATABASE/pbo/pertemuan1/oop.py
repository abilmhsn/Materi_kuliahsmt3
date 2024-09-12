
class luas:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def luas_persegipanjang(self):
        return self.panjang * self.lebar
cek_luas = luas(7,10)
print(f"luas persegi adalah {cek_luas.luas_persegipanjang()}")