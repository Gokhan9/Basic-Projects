# Cinsiyet ve boy uzunluğuna göre mülakatı geçme örneği.
    # Pilotluk sınavında adayların ilk aşamayı geçebilmesi için bir ön koşul koyulmuştur. Bunlar:
    # Cinsiyeti kadın olanlar için 1.64
    # Cinsiyeti erkek olanlar için 1.82
    # Boy sınırını geçtiği takdirde ön sağlık muaynesine geçebilirler.

cinsiyet = input("Lütfen Cinsiyetinizi Belirtiniz: ")
boy = int(input("Lütfen Boy Ölçünüzü Giriniz: "))
kg = int(input("Lütfen Kilonuzu Giriniz:"))

if cinsiyet == "Erkek" or cinsiyet == "Kadın" and (boy > 15 or boy < 300) and (kg > 54 or kg < 85):
    if cinsiyet == "Kadın" and boy >= 164 and kg <= 54:
        print("Tebrikler! Bir sonraki aşamaya geçtiniz.")
    elif cinsiyet == "Erkek" and boy >= 182 and kg <= 85:
        print("Tebrikler! Bir sonraki aşamaya geçtiniz.")
    else:
        print("Mülakat Aşamasından Elendiniz.")
else:
    print("Hatalı İşlem Yaptınız. Size verilen yönerge doğrultusunda işlem yapmaya özen gösteriniz. İyi Günler.")