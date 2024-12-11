from Animal import *

class Ikan(Animal):
    def __init__(self,nama,makanan,hidup,berkembang_biak,jenis,warna):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.jenis = jenis
        self.warna = warna
    def cetak_ikan(self):
        super().cetak()
        print("Jenis\t\t: ",self.jenis,"\nWarna\t\t: ",self.warna)

paus = Ikan("Paus", "Ikan Kecil", "laut","Melahirkan","Mamalia","Biru")
paus.cetak_ikan()
mujair = Ikan ("Mujair", "Lumut", "Sungai","Bertelur","Ikan Air Tawar","Abu-abu")
mujair.cetak_ikan()