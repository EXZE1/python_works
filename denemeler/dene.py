class yazilimci():

    def __init__(self,isim,soyisim,numarasi,maaş,deneyim_yili,diller):

        self.isim=isim
        self.soyisim=soyisim
        self.numarasi=numarasi
        self.maaş=maaş
        self.deneyim_yili=deneyim_yili
        self.diller=diller
    def bilgilerigöster(self):
        print(""" Yazilimci bilgileri...
        isim : {}
        soyisim : {}
        numarasi : {}
        maaş : {}
        deneyim : {}
        diller : {}

        """.format(self.isim,self.soyisim,self.numarasi,self.maaş,self.deneyim_yili,self.diller))
yazili = yazilimci("oguzhan","yucedag",00000,1000000,4,["java","python","C","C#","C+"])
yazili.bilgilerigöster()
