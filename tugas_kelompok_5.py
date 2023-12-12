# kelompok 5
#  1. Dyah Prameswari Cinta Herlianti [5220411312]
#  2. Vina Nasyi Atul Lailiyah  [5220411282]

class Animal :
    def __init__(self, Nama, Sifat, Ukuran, Jumlah_kaki):
        self.nama = Nama 
        self.sifat = Sifat 
        self.ukuran = Ukuran 
        self.jmlh_kaki = Jumlah_kaki

class Mamalia(Animal):
    def __init__(self, Nama, Sifat, Ukuran, Jumlah_kaki, Bisa_jalan, Jenis_Mamalia):
        super().__init__(Nama, Sifat, Ukuran, Jumlah_kaki)
        self.jalan = Bisa_jalan
        self.mamalia = Jenis_Mamalia

class Aves(Animal):
    def __init__(self, Nama, Sifat, Ukuran, Jumlah_kaki, Bisa_terbang, Jenis_Aves):
        super().__init__(Nama, Sifat, Ukuran, Jumlah_kaki)
        self.terbang = Bisa_terbang
        self.aves = Jenis_Aves

class Ayam(Aves):
    def __init__(self, Nama, Sifat, Ukuran, Jumlah_kaki, Bisa_terbang, Jenis_Aves, Jenis_Ayam, Bisa_diadu):
        super().__init__(Nama, Sifat, Ukuran, Jumlah_kaki, Bisa_terbang, Jenis_Aves)
        self.ayam = Jenis_Ayam
        self.diadu = Bisa_diadu


# Objek Animal : 
animal_1 = Animal ("Mamalia","Karnivora/Hebivora","Besar/kecil","Ada 4 Kaki",)
animal_2 = Animal ("Aves","Biji-bjian/Oportunistik","Besar/kecil","Ada 2 Kaki",)
 
# Objek Mamalia 
mamalia_1 = Mamalia ("Mamalia","Karnivora","Besar","Ada 4 Kaki","Berjalan dan Berlari","Singa")
mamalia_2 = Mamalia ("Mamalia","Hebivora","Besar","Ada 4 Kaki","Berjalan dan Berlari","Kuda")
mamalia_3 = Mamalia ("Mamalia","Hebivora","Besar","Ada 4 Kaki","Berjalan dan Berlari","Gajah")

# Objek Aves :
Aves_1 = Aves ("Aves","Biji-Bijian","kecil","Ada 2 Kaki","Terbang","Merpati")
Aves_2 = Aves ("Aves","Oportunistik","kecil","Ada 2 Kaki","Terbang","Camar")

# Objek Ayam :
ayam_ = Ayam ("Aves","Biji-bijian","Kecil","Ada 2 Kaki","Bisa terbang/ Bisa tidak terbang","Ayam","Ayam Ternak","Tidak Bisa diadu")

# Output Keseluruhan :
print ("~~~~~~~~~~~~ Daftar Hewan-Hewan ~~~~~~~~~~~~")
print ("____________________________________________")
print ("")
print ("Katagori Hewan :")
print ("")
print ("Jenis Hewan   : ", animal_1.nama)
print ("Sifat/Pemakan : ",animal_1.sifat)
print ("Ukuran Hewan  : ",animal_1.ukuran)
print ("Jumlah Kaki   : ",animal_1.jmlh_kaki)
print ("____________________________________________")
print ("")
print ("Katagori Hewan :")
print ("")
print ("Jenis Hewan   : ", animal_2.nama)
print ("Sifat/Pemakan : ",animal_2.sifat)
print ("Ukuran Hewan  : ",animal_2.ukuran)
print ("Jumlah Kaki   : ",animal_2.jmlh_kaki)
print ("____________________________________________")
print ("")
print ("Katagori Hewan :")
print ("")
print ("Jenis Hewan   : ", mamalia_1.nama)
print ("Sifat/Pemakan : ", mamalia_1.sifat)
print ("Ukuran Hewan  : ", mamalia_1.ukuran)
print ("Jumlah Kaki   : ", mamalia_1.jmlh_kaki)
print ("Tipe Hwan     : ", mamalia_1.jalan)
print ("Nama Hewan    : ", mamalia_1.mamalia)
print ("____________________________________________")
print ("")
print ("Katagori Hewan :")
print ("")
print ("Jenis Hewan   : ", mamalia_2.nama)
print ("Sifat/Pemakan : ", mamalia_2.sifat)
print ("Ukuran Hewan  : ", mamalia_2.ukuran)
print ("Jumlah Kaki   : ", mamalia_2.jmlh_kaki)
print ("Tipe Hwan     : ", mamalia_2.jalan)
print ("Nama Hewan    : ", mamalia_2.mamalia)
print ("____________________________________________")
print ("")
print ("Katagori Hewan :")
print ("")
print ("Jenis Hewan   : ", mamalia_3.nama)
print ("Sifat/Pemakan : ", mamalia_3.sifat)
print ("Ukuran Hewan  : ", mamalia_3.ukuran)
print ("Jumlah Kaki   : ", mamalia_3.jmlh_kaki)
print ("Tipe Hwan     : ", mamalia_3.jalan)
print ("Nama Hewan    : ", mamalia_3.mamalia)
print ("____________________________________________")
print ("")
print ("Katagori Hewan :")
print ("")
print ("Jenis Hewan   : ", Aves_1.nama)
print ("Sifat/Pemakan : ", Aves_1.sifat)
print ("Ukuran Hewan  : ", Aves_1.ukuran)
print ("Jumlah Kaki   : ", Aves_1.jmlh_kaki)
print ("Tipe Hwan     : ", Aves_1.terbang)
print ("Nama Hewan    : ", Aves_1.aves)
print ("____________________________________________")
print ("")
print ("Katagori Hewan :")
print ("")
print ("Jenis Hewan   : ", Aves_2.nama)
print ("Sifat/Pemakan : ", Aves_2.sifat)
print ("Ukuran Hewan  : ", Aves_2.ukuran)
print ("Jumlah Kaki   : ", Aves_2.jmlh_kaki)
print ("Tipe Hwan     : ", Aves_2.terbang)
print ("Nama Hewan    : ", Aves_2.aves)
print ("____________________________________________")
print ("")
print ("Katagori Hewan :")
print ("")
print ("Jenis Hewan     : ", ayam_.nama)
print ("Sifat/Pemakan   : ", ayam_.sifat)
print ("Ukuran Hewan    : ", ayam_.ukuran)
print ("Jumlah Kaki     : ", ayam_.jmlh_kaki)
print ("Tipe Hwan       : ", ayam_.terbang)
print ("Nama Hewan      : ", ayam_.aves)
print ("Jenis Ayam      : ", ayam_.ayam)
print ("diadu/tdk diadu : ", ayam_.diadu)
print ("")
print ("")
print ("____________________________________________")
