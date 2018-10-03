"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

text = input("Enter e to encrypt, d to decrypt, or q to quit: ")

while text != "q":
    if text != "e" and text != "d":
        print("Did not understand command, try again.")
    elif text = "e":
        message = input("Message: )
        key = input("Key: ")
    

"""
def repeat_this(text):
    print(text)

if text != "e" and text != "q":
    print("Did not understand command, try again.")


if text == "e":
    message = input("Message: ")
    key = input("Key: ")
def repeat_this(tex):
    print(text)

"""


#scramble = associations.find(message)
#print(scramble)