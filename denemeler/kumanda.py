import random
import time
class Kumanda():

    def __init__(self,tv_durum = "Kapali",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):

        self.tv_durum = tv_durum

        self.tv_ses =tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

        

    def tv_ac(self):

        if (self.tv_durum == "Açik"):
            print("tv zaten açik.")

        else:
            print("tv açiliyor...")
            self.tv_durum = "Açik"

    def tv_kapat(self):
        if (self.tv_durum == "Kapali"):
            print("tv zaten kapali.")

        else:
            print("tv kapaniyor...")
            tv_durum ="Kapali"

    def ses_ayarlari(self):
        
        while True:
            
            cevap = input("Sesi Azalat: '<' \nSesi Artir: '>'\nÇikiş: çikiş\n...: ")

            if (cevap == "<"):
                if (self.tv_ses != 0):

                    self.tv_ses -=1
                    print("Ses:",self.tv_ses)
            elif (cevap == ">"):
                if (self.tv_ses != 31):

                    self.tv_ses += 1

                    print("Ses",self.tv_ses)
            else:
                print("Ses gücellendei:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append()

        print("Kanal eklendi...")

    def rasgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)+1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki kanal:",self.kanal)

    def __len__(self):

        return len(self.kanal_listesi)
    
    def __str__(self):

        return "Tv durum: {}\nTv ses: {}\nKanal listesi {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.tv_kanal_listesi,self.kanal)
        
kumanda = Kumanda()

print(""" 
televizyon uygulamasi

1. tv aç

2. tv kapa 

3. ses 

4. kanal ekle 

5. kanal sayisini öğrenme 

6. rasgele kanal geçme 

7. tv bilgileri 

çikmak için 'q' ya basin.

""")

while True:

    işlem = input("işlem seçiniz:")

    if (işlem == "q"):
        print("işlem sonlandiriliyor...")
        break

    elif (işlem == "1"):
        kumanda.tv_ac()

    elif(işlem == "2"):
        kumanda.tv_kapat()

    elif(işlem == "3"):
        kumanda.ses_ayarlari()

    elif ( işlem == "4"):
        kanal_isimleri = input("Kanal isimleri ',' ile ayrirarak girin:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif (işlem == "5"):
        print("Kanal Sayisi :",len(kumanda))

    elif (işlem == "6"):
        kumanda.rasgele_kanal()

    elif (işlem == "7"):
        print(kumanda)

    else:
        print("geçersiz işlem...")
