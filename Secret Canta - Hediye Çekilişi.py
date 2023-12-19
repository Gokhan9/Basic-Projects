import random   #Rastgele isim,sayı seçileceği zamana çağırılması gereken komut.

names = ["Gökhan", "Burak", "Edin", "Emre", "Oktay", "Erman", "Kaan", "Gizem", "Çağrı", "Pınar"]

def gift():
    hediyeAlanlar = names.copy()
    hediyeVerenler = names.copy()

    while len(hediyeAlanlar) > 0:   # Listede ki eleman kadar işlemi devam ettiricek.

        alici = random.randint(0, len(hediyeAlanlar) -1 )
        verenler = random.randint(0, len(hediyeVerenler) -1 )

        while hediyeVerenler[alici] == hediyeVerenler[verenler]:
            alici = random.randint(0, len(hediyeAlanlar)-1)
            verenler = random.randint(0, len(hediyeVerenler)-1)


        print(hediyeAlanlar[alici], "kime hediye alacak? :", hediyeVerenler[verenler])
        del hediyeAlanlar[alici]
        hediyeVerenler.remove(hediyeVerenler[verenler])

gift()