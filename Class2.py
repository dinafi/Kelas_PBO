class student():
    def _init_(self, a,b,c,d):
        self.full_name = a
        self.age = b
        self.alamat = c
        self.status = d
    def get_age(self):
        return self.age
    def get_alamat(self):
        return self.alamat
    def get_status(self):
        return self.status

f = student("Banda Subaja", 20, "Bandung", "Mahasiswa")
print("Nama   : ", f.full_name)
print("Usia   : ", f.get_age())
print("Alamat : ", f.get_alamat())
print("Status : ", f.get_status())