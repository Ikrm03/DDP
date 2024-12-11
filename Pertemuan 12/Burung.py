from Animal import *

class Burung (Animal):
    def __init__(self,nama,makanan,hidup,berkembang_biak,jenis,warna):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.jenis = jenis
        self.warna = warna
    def cetak_burung(self):
        super().cetak()
        print("Jenis\t\t: ",self.jenis,"\nWarna\t\t: ",self.warna)

jalak= Burung("Jalak", "Pisang", "Darat","Bertelur","Kicau","Hitam")
jalak.cetak_burung()
beo = Burung('Beo','Jagung','Bertelur','Darat','Paruh Bengkok','Putih')
beo.cetak_burung()