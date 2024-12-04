class kullanici():
    def __init__(self, ad , hesapNumarasi , baslangicBakiyesi):
        self.ad = ad
        self.hesapNumarasi = hesapNumarasi
        self.baslangicBakiyesi = baslangicBakiyesi

    def __str__(self):
        return f"{self.ad} - {self.hesapNumarasi} - {self.baslangicBakiyesi}"
    
    def bakiyeSorgula(self):
        print(f"{self.ad} adlı kullanıcının bakiyesi: {self.baslangicBakiyesi} TL")

    def paraYatir(self ,miktar):
        if miktar > 0:
            self.baslangicBakiyesi = float(self.baslangicBakiyesi)
            self.baslangicBakiyesi += float(miktar)
            print(f"{miktar} TL yatırıldı. Güncel bakiye: {self.baslangicBakiyesi} TL")
        else:
            print("Geçersiz miktar. Pozitif bir rakam girin.")

    def paraCek(self, miktar):
        if miktar > 0:
            if miktar <= self.baslangicBakiyesi:
                self.baslangicBakiyesi -= miktar
                print(f"{miktar} TL çekildi. Güncel bakiye: {self.baslangicBakiyesi} TL")
            else:
                print("Yetersiz bakiye.")
        else:
            print("Geçersiz miktar. Pozitif bir rakam girin.")

class banka():
    def __init__(self):
        self.kullanici_listesi =[]
    
    def olustur(self):
        ad = input("Ad girisi: ")
        hesapNumarasi = input("Hesap numarasi girisi: ")
        baslangicBakiyesi = input("Balangıç bakiyesi girisi: ")

        yeni_kullanici = kullanici(ad , hesapNumarasi , baslangicBakiyesi)
        self.kullanici_listesi.append(yeni_kullanici)
        print(f"{ad} adlı kullanici oluşturuldu.")
 

    def listele(self):
        if len(self.kullanici_listesi) == 0:
            print("Henüz kullanıcı eklenmemiş.")
        else:
            for kullanici in self.kullanici_listesi:
                print(kullanici)

    def kullanici_bul(self, hesapNumarasi):
        for kullanici in self.kullanici_listesi:
            if kullanici.hesapNumarasi == hesapNumarasi:
                return kullanici
        print("Hesap numarası bulunamadı.")
        return None
    

if __name__ == "__main__":
    banka_sistemi = banka()
    while True:
        print("\n1. Kullanıcı oluştur")
        print("2. Kullanıcıları listele")
        print("3. Para yatırma")
        print("4. Para çekme")
        print("5. Bakiye sorgulama")
        print("6. Çık")
        
        secim = input("Seçiminizi yapın (1/2/3/4/5/6): ")

        if secim == "1":
            banka_sistemi.olustur()
        elif secim == "2":
            banka_sistemi.listele()
        elif secim == "3":
            hesapNumarasi = input("Hesap numarasını girin: ")
            kullanici = banka_sistemi.kullanici_bul(hesapNumarasi)
            if kullanici:
                miktar = float(input("Yatırılacak miktarı girin: "))
                kullanici.paraYatir(miktar)
        elif secim == "4":
            hesapNumarasi = input("Hesap numarasını girin: ")
            kullanici = banka_sistemi.kullanici_bul(hesapNumarasi)
            if kullanici:
                miktar = float(input("Çekilecek miktarı girin: "))
                kullanici.paraCek(miktar)
        elif secim == "5":
            hesapNumarasi = input("Hesap numarasını girin: ")
            kullanici = banka_sistemi.kullanici_bul(hesapNumarasi)
            if kullanici:
                kullanici.bakiyeSorgula()
        elif secim == "6":
            break
        else:
            print("Geçersiz seçim!")

