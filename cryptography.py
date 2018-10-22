"""
cryptography.py
Author: Patrick Daley
Credit: <list sources used, if any>
Assignment:
Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
import string

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

text = input("Enter e to encrypt, d to decrypt, or q to quit: ")

while text != "q" and text != "e" and text != "d":
    print("Did not understand command, try again.")
    text = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if text == "e":
    message = input("Message: ")
    key = input("Key: ")
   
    if len(message) == len(key):
        for m in message:
            ma = associations.find(m)
            for k in key:
                ka = associations.find(k)
                encrypt = ma + ka
                print(associations[encrypt], end="")
        
    elif len(message) < len(key):
        print("hi")
    elif len(message) > len(key):
        print("hello")

#----------------------------------------------------------------------------
elif text == "d":
    message = input("Message: ")
    key = input("Key: ")
    
    for m in message:
        ma = associations.find(m)
        for k in key:
            ka = associations.find(k)
            decrypt = ma-ka
            print(associations[decrypt], end="")

elif text == "q":
    print("Goodbye!")
