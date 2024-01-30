# YÖNERGE = Vize %30, kısa sınav 1 ve 2 toplam %20, final ise %50 etkilemektedir.
# YÖNERGE = Ders ortalaması 50 ve altı olan öğrenciler başarısız sayılırken, 50 ve üstü öğrenciler başarılı sayılmaktadır.

vize1 = int(input("Vize Notunuzu Giriniz: "))
kisaSinav1 = int(input("1. Kısa Sınav Notunuzu Giriniz: "))
kisaSinav2 = int(input("2. Kısa Sınav Notunuzu Giriniz: "))
final1 = int(input("Final Notunuzu Giriniz: "))

if final1 >= 50:
    ortHesabi = vize1 * 0.3 + kisaSinav1 * 0.1 + kisaSinav2 * 0.1 + final1 * 0.5
    if ortHesabi > 50:
        print("{} Ders Ortalaması ile geçtiniz.".format(ortHesabi))
    elif ortHesabi < 50:
        print("{} Ders Ortalaması ile kaldınız.".format(ortHesabi))