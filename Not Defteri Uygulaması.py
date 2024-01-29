dosyaAdi = "Notlar.txt"

def notEkle():
    notMetinİcerigi = input("Notunuzu Giriniz:")
    with open(dosyaAdi, "a") as dosya:
        dosya.write(notMetinİcerigi + "\n")
    print("Başarıyla Eklendi.")

def notGoruntule():
    try:
        with open(dosyaAdi , "r") as dosya:
            notlar = dosya.readlines()
            if notlar:
                print("Notlarınız:")
                for notSatiri in notlar:
                    print(notSatiri.strip())
            else:
                print("Not henüz eklenmemiş.")
    except FileNotFoundError:
        print("Not dosyası bulunamadı!")

while True:
    print("\n1 - Not Ekle")
    print("2 - Notları Görüntüle")
    print("3 - Çıkış")

    sec = input("Bir seçeneği seçerek yapmak istediğiniz işleme devam Edebilirsiniz. (1 - 2 - 3): ")

    if sec == "1":
        notEkle()
    elif sec == "2":
        notGoruntule()
    elif sec == "3":
        print("Program Çıkışı Yapılıyor.")
        break
    else:
        print("Geçersiz seçenek. Lütfen 1, 2 veya 3 seçeneğini girin.")