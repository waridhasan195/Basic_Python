
import random
from random import sample
import qrcode

def password_generator(pass_length):
    upperChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerChar = upperChar.lower()
    digits = '0123456789'
    spacialChar = "`~!@#$%>^&*()_+-*/<\|;:"
    passwordList = upperChar + lowerChar + digits + spacialChar
    password = ''.join(random.sample(passwordList, pass_length))
    return password

def qrcode_generator(password):
    file_name = str(input("Type Your file name:"))
    img = qrcode.make(password)
    img.save(file_name + ".png")


def userinput():
    while True:
        try:
            pass_length = int(input("Please Input Password Length: "))
            return pass_length
            break
        except:
            print("Please Enter Valid Interger Number:")


if __name__ == '__main__':
    pass_length = userinput()
    password_generator_variable = password_generator(pass_length)
    print("Password is: ", password_generator_variable)
    qrcode_generator(password_generator_variable)


