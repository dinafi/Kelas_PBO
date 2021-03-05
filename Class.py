class student:

    def nama(self):
        print("Nama   : "), self.full_name
    def get_age (self):
        print("Usia   : "), self.age
    def get_alamat (self):
        print("Alamat : "), self.address
    budi = student()
    
    budi.full_name = "Budi Doremi"
    budi.age = "30"
    budi.adderss = "Menteng, Jakarta usat"
    
    budi.nama()
    budi.get_age()
    budi.address()
    