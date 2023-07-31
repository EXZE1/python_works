class Araba():

    def __init__(self,marka,model,uretim_yili,motor_hacmi,rengi):
        print("init")

        self.marka = marka

        self.model = model

        self.uretim_yili = uretim_yili

        self.motor_hacmi = motor_hacmi

        self.rengi = rengi

    def marka(self):
        kullanici=int(input("""
        
        ***HANGİ MARKA ARABA KIYASLAMAK İSTERSİNİZ***

        1 === TESLA

        2 === PORSCHE

        3 === MERCEDES

        4 === BMW
        
        """))
araba=Araba()
araba.marka()
    

