import random

c_letters = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","x","q","w"]
l_letters = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","Q","W","X"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
special_characters = [".",",","!","?","_"]

while True:                                                                  #detects user errors
    length = input("Choose the password length: ")
    try:
        length = int(length)
        if length < 8:
            print("The password cannot be less than 8 characters!")
        else:
            break
    except ValueError:
        print("Please enter a valid number!")

password = []
c_let = random.choice(c_letters)                                             #ensures that the password contains at least one of each character
password.append(c_let)
l_let = random.choice(l_letters)
password.append(l_let)
num = random.choice(numbers)
password.append(num)
spec = random.choice(special_characters)
password.append(spec)

total = c_letters + l_letters + numbers + special_characters
for a in range(length - 4):                                                  #chooses random characters from four different types
    char = random.choice(total)
    password.append(char)

random.shuffle(password)
pword = "".join(password)
print("The password: ", pword)

