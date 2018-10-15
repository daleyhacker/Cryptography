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
    
    for m in message:
        ma = associations.find(m)
        for k in key:
            ka = associations.find(k)
            encrypt = (ma)+(ka)
            print(encrypt)
            print(associations[encrypt], end="")
 
    
    

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


   
    """
    for m in message:
        ma = associations.find(m)
        print(ma)
    
    for k in key:
        ka = associations.find(k)
        print(ka)
    
    for x in ma:
        print(x[0], x[1])
    

    
    
    #print(associations[9])

-----------------------------------------------

if text == "e":
    message = input("Message: ")
    key = input("Key: ")
    m1 = list(message)
    k1 = list(key)
    m2 = associations.find(m1)
    k2 = assocations.find(k1)
    z = zip(m1, k1)
    for x in z:
        print(x[0], x[1])
"""
