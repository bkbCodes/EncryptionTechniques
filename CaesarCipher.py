def encrypt(msg, key):
    cipher = ""
    for i in msg:
        if i.isdigit():
            cipher += chr( (ord(i)-ord('0')+key)%10 + ord('0') )
        elif i.islower():
            cipher += chr( (ord(i)-ord('a')+key)%26 + ord('a') )
        elif i.isupper():
            cipher += chr( (ord(i)-ord('A')+key)%26 + ord('A') )
        else:
            cipher += i
    return cipher

def decrypt(cipher, key):
    key = -key
    return encrypt(cipher, key)

msg = "hello World, this is rot 13"
key = 13
cipher = encrypt(msg, key)
receivedMsg = decrypt(cipher, key)
print(cipher)
print(receivedMsg)