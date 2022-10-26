class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a
        
    def __str__(self):
        return "yazdırılan : " + self.metin   
        
nesne = sinif("Civa")
print(nesne)  