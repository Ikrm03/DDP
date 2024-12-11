class Animal : 
    def __init__(self,nama,makanan,hidup,berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print('\nnama\t\t: ',self.nama,
              '\nmakanan\t\t: ', self.makanan,
              '\nhidup\t\t: ',self.hidup,
              '\nberkembang_biak : ' , self.berkembang_biak)


objek = Animal('Buaya',"Daging",'Amphibi',"bertelur")
objek.cetak()

