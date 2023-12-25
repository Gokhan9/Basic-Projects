import random

sayi = random.randint(1, 25)
hak = 5
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin Ettiğiniz Sayıyı Giriniz: "))

    if sayi == tahmin:
        print(f"Tebrikler. {sayac}. defada bildiniz. Tuttuğum Sayı: {sayi} , Puan: {70-10 * (sayac-1)}")
        break

    elif sayi > tahmin:
        print("Tahmininiz sayıdan küçük. Biraz daha büyük bir sayı giriniz.")
    else:
        print("Biraz daha küçük sayı giriniz.")

    if hak == 0:
        print(f"Hakkınız Tükendi. Tuttuğum Sayı: {sayi}")