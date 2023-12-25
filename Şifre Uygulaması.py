import random
import string

numbers = string.digits
symbols = string.punctuation #for symbols
lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
allCharacters = [lowerLetters, numbers, upperLetters, symbols]

print(numbers)
print(symbols)
print(lowerLetters)
print(upperLetters)

password = ""

# for i in range(2):
#     password += allCharacters[0][random.randint(0, 9)]
# for i in range(2):
#     password += allCharacters[1][random.randint(0, 9)]
# for i in range(2):
#     password += allCharacters[2][random.randint(0, 9)]
# for i in range(2):
#     password += allCharacters[3][random.randint(0, 9)]

for j in range(4):      # Yukarıda ki kod bloğunun kısa ve daha kullanışlı hali.
    for i in range(2):
        password += allCharacters[j][random.randint(0, 9)]

password = list(password)   
random.shuffle(password)    #Şifreyi belli bir sıraya tabii tutmadan karıştırma komutunu kullandık.
print(password)



newPassword = ""

# for i in password:
#     newPassword += i

newPassword = newPassword.join(password)

print(newPassword)