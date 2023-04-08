#nasıl araba istiyorsunuz
class Araba():
    def __init__(self,model,renk,beygir_gucu,silindir):
        print("init fonksiyonu calistirildi")
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir

    def get_model(self):
        return self.model
    
araba = Araba("pegeout","kırmızı","300",4)
model = araba.get_model()

print(model)
print(araba.model)
