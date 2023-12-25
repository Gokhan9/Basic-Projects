from random import randint

r = randint(1,100)
sayac = 0


while True:
    sayac += 1
    sayi = int(input("Lütfen 1-100 Arası Bir Değer Giriniz: "))

    if sayi == 0:
        print("Harika")
        break
    elif sayi > r:
        print("Daha Küçük bir veri girmelisin!")
        continue
    elif sayi < r:
        print("DAHA BÜYÜK BİR VERİ GİRMELİSİN!")
        continue
    else:
        print("Rastgele Sayı: ", r)
        print("Kaçıncı Defada Tahmin Ettiniz: ", sayac)
