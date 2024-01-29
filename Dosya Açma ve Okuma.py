# Dosya Açma - Write
with open("Dosya.txt", "w") as dosya:
    dosya.write("Dosya Açma İşlemleri. ")

# Dosya Okuma - Read
with open("Dosya.txt", "r") as dosya:
    okuma = dosya.readline()
    print("Dosyanın İçeriği:", okuma)