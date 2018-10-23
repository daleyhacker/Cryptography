"""
cryptography.py
Author: Patrick Daley
Credit: <list sources used, if any>
Assignment:
Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""


associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

text = input("Enter e to encrypt, d to decrypt, or q to quit: ")

while text != "q" and text != "e" and text != "d":
    print("Did not understand command, try again.")
    text = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if text == "e":
    message = input("Message: ")
    key = input("Key: ")
   
    if len(message) == len(key):
        for x in zip(message, key):
            x0 = x[0]
            x1 = x[1]
            x0a = associations.find(x0)
            x1a = associations.find(x1)
            encrypt = x0a + x1a
            print(associations[encrypt], end="")
            
    elif len(message) < len(key):
        for x in zip(message, key):
            x0 = x[0]
            x1 = x[1]
            x0a = associations.find(x0)
            x1a = associations.find(x1)
            encrypt = x0a +x1a
            print(associations[encrypt], end="")
    elif len(message) > len(key):
        for x in zip(message, key):
            x0 = x[0]
            x1 = x[1]
            x0a = associations.find(x0)
            x1a = associations.find(x1)
            while x1a < x0a:
                x1a = str(x1a) + str(x0)
            encrypt = x0a + x1a
            print(associations[encrypt], end="")

#----------------------------------------------------------------------------
elif text == "d":
    message = input("Message: ")
    key = input("Key: ")
    if len(message) == len(key):
        for x in zip(message, key):
                x0 = x[0]
                x1 = x[1]
                x0a = associations.find(x0)
                x1a = associations.find(x1)
                encrypt = x0a - x1a
                print(associations[encrypt], end="")
    
    if len(message) > len(key):
        print(hi)
                
    elif len(message) < len(key):
        for x in zip(message, key):
                x0 = x[0]
                x1 = x[1]
                x0a = associations.find(x0)
                x1a = associations.find(x1)
                encrypt = x0a - x1a
                print(associations[encrypt], end="")

elif text == "q":
    print("Goodbye!")
