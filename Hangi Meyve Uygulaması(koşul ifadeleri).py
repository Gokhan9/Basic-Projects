def hangiMeyve():
    ay = input("\nBir Ay Giriniz: ")
    gün = int(input("Bir Gün Giriniz: "))

    if ay == "Ocak" or ay == "Şubat":
        meyve = "Portakal"
    elif ay == "Mart" or ay == "Nisan":
        meyve = "Karpuz"
    elif ay == "Mayıs" or ay == "Haziran":
        if gün < 15:
            meyve = "Yeşil Elma"
        else:
            meyve = "Kırmızı Elma"    
    elif ay == "Temmuz" or ay == "Ağustos":
        if gün > 20:
            meyve = "Üzüm"
        else:
            meyve = "Böğürtlen"
    elif ay == "Eylül" or ay == "Ekim":
        meyve = "Karadut"
    elif ay == "Kasım" or "Aralık":
        meyve = "Şeftali"
        
    print(gün, ay, "günü", meyve, "yiyebilirsiniz.")

hangiMeyve()
    