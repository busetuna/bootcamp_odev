class Film:
    def __init__(self, ad, yonetmen, yil, turBilgisi):
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil
        self.turBilgisi = turBilgisi

    def __str__(self):
        return f"{self.ad} - {self.yonetmen} - {self.yil} - {self.turBilgisi}"


class FilmYoneticisi:
    def __init__(self):
        self.listeler = []

    def filmEkle(self):
        # Kullanıcıdan film bilgilerini alıyoruz
        ad = input("Film adı girin: ")
        yonetmen = input("Yönetmen adı girin: ")
        yil = int(input("Yıl girin: "))
        turBilgisi = input("Tür bilgisi girin: ")

        # Film nesnesi oluşturuluyor ve listeye ekleniyor
        film_ekle = Film(ad, yonetmen, yil, turBilgisi)
        self.listeler.append(film_ekle)
        print(f"{ad} adlı film başarıyla eklendi.")

    def filmSil(self):
        # Kullanıcıdan silmek istediği film ismini alıyoruz
        ad = input("Silmek istediğiniz filmin adını girin: ")
        for film in self.listeler:
            if film.ad.lower() == ad.lower():  # İsim eşlemesi büyük/küçük harfe duyarsız
                self.listeler.remove(film)
                print(f"{ad} adlı film başarıyla silindi.")
                return
        print(f"{ad} adlı film listede bulunamadı.")

    def filmListele(self, filtre=None, deger=None):
        # Filmleri listeleme işlemi
        if filtre == "yil":
            # Yıla göre filtreleme
            for film in self.listeler:
                if film.yil == deger:
                    print(film)
        elif filtre == "tur":
            # Tür bilgisine göre filtreleme
            for film in self.listeler:
                if film.turBilgisi.lower() == deger.lower():
                    print(film)
        else:
            # Filtreleme yoksa tüm filmleri listeleme
            for film in self.listeler:
                print(film)


# Uygulamanın çalışma örneği
yonetici = FilmYoneticisi()

# Film ekleme
yonetici.filmEkle()

# Film listeleme (yıla göre)
print("\n2020 yılına ait filmler:")
yonetici.filmListele(filtre="yil", deger=2020)

# Film listeleme (türe göre)
print("\nAksiyon türündeki filmler:")
yonetici.filmListele(filtre="tur", deger="Aksiyon")

# Film silme
yonetici.filmSil()

# Tüm filmleri listeleme
print("\nTüm filmler:")
yonetici.filmListele()
