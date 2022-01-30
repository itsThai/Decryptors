def decrypt(string):
    for i in range(26):
        cipher = ''
        for char in string:
            if char == ' ':
                cipher = cipher + char
            elif  char.isupper():
                cipher = cipher + chr((ord(char) + i - 65) % 26 + 65)
            else:
                cipher = cipher + chr((ord(char) + i - 97) % 26 + 97)
        print(i, cipher)


def encrypt(string, number):
    cipher = ''
    for char in string:
            if char == ' ':
                cipher = cipher + char
            elif  char.isupper():
                cipher = cipher + chr((ord(char) + number - 65) % 26 + 65)
            else:
                cipher = cipher + chr((ord(char) + number - 97) % 26 + 97)
    print(cipher, "with the shift", number)

def decrypt1(string, shift):
    i = 26 - shift
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + i - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + i - 97) % 26 + 97)
    print(cipher)


text = input("enter string: ")
print("original string: ", text)
a = int(input("0 for decrypt, 1 for encrypt: "))
if a == 0:
    b = int(input("do you know the shift, 0 for no, 1 for yes:"))
    if b ==0:
        print("Tried all the shifts:")
        decrypt(text)
    else:
        c = int(input("what the shift: "))
        print("Decrypt", text, "with shift", c)
        decrypt1(text,c)
else:
    number = int(input("choose the shift: "))
    print("Your encrypted text: ")
    encrypt(text, number)