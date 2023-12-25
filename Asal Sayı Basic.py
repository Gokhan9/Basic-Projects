"""
SORU: Girilen bir sayının asal olup olmadığını bulun.
** Asal SAYI 1 ve kendisi hariç tam böleni olmayan sayılara denir.
"""

sayi = int(input("Bir Sayı Giriniz: "))
asalMi = True

if sayi == 1:
    asalMi = False

for i in range(2, sayi):
    if sayi % i == 0:
        asalMi = False
        break

if asalMi:
    print("Asaldır")
else:
    print("Asal Sayı Değildir.")