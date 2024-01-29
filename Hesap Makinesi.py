def topla(x,y):
    return x + y

def cikar(x,y):
    return x - y

def carp(x,y):
    return x * y

def bol(x,y):
    if y != 0:
        return x / y
    else:
        return "Hata"

s1 = float(input("1. Sayı:"))
s2 = float(input("2. Sayı:"))

print("Toplam:", topla(s1,s2))
print("Çıkar:", cikar(s1,s2))
print("Çarp:", carp(s1,s2))
print("Böl:", bol(s1,s2))