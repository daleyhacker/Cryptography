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

while text != "q" and text != "e" and text != "d":
    print("Did not understand command, try again.")
    text = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if text == "e":
    message = input("Message: ")
    key = input("Key: ")
    message1 = list(message)
    key1 = list(key)
    #m = associations.find(message1)
    #k = assocations.find(key1)
    z = zip(message1, key1)
    for x in z:
        print(x[0], x[1])

elif text == "d":
    message = input("Message: ")
    text = input("Key: ")

elif text == "q":
    print("Goodbye!")