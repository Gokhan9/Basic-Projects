GokhanHesap = {
    "Ad": "Gökhan",
    "Soyad": "CÖMERT",
    "Hesap No": 1242131,
    "Hesap Bakiyesi": 4050,
    "Ek Hesap Bakiyesi": 2100
}

GizemHesap = {
    "Ad": "Gizem",
    "Soyad": "CÖMERT",
    "Hesap No": 561235,
    "Hesap Bakiyesi": 5025,
    "Ek Hesap Bakiyesi": 400
}

def paraCek(hesap, miktar):
    print(f"Hoşgeldin {hesap['Ad']}")

    if (hesap["Hesap Bakiyesi"] >= miktar):
        hesap["Hesap Bakiyesi"] -= miktar
        print("Paranızı Çekebilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["Hesap Bakiyesi"] + hesap["Ek Hesap Bakiyesi"]

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek Hesap Kullanımı Yapmak İstiyor musunuz? (Evet / Hayır): ")

            if ekHesapKullanimi == "Evet":
                ekHesaptanKullanilicakMiktar = miktar - hesap["Hesap Bakiyesi"]
                hesap["Hesap Bakiyesi"] = 0
                hesap["Ek Hesap Bakiyesi"] -= ekHesaptanKullanilicakMiktar
                print("Ek Hesap Kullanımı Yapabilirsiniz.")
                bakiyeSorgula(hesap)
            
            else:
                print(f"{hesap['Hesap No']} nolu hesapta {hesap['Hesap Bakiyesi']} bulunmaktadır.")
        else:
            print("Yetersiz Bakiye.")

def bakiyeSorgula(hesap):
    print(f"{hesap['Hesap No']} nolu hesabınızda, {hesap['Hesap Bakiyesi']} bulunmaktadır. Ek hesap içerisinde yer alan limitiniz ise {hesap['Ek Hesap Bakiyesi']} TL'dir.")

paraCek(GokhanHesap, 4050)
print("*")
paraCek(GokhanHesap, 200)
