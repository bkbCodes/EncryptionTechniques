# sub encrpytion function Caesar Cipher
from CaesarCipher import encrypt as f

# Xor of two equal strings
def XOR(m1,m2):
    out = ""
    for i in range(len(m1)):
        n1 = ord(m1[i]) - ord("A")
        n2 = ord(m2[i]) - ord("A")
        out += chr(ord("A") + (n1^n2))
    return out

# Encryption function Feistel Cipher
def encrypt(msg,key):
    if len(msg) % 2 == 1:
        msg+='x'
    Lhalf = msg[0:len(msg)//2]
    Rhalf = msg[len(msg)//2:]
    for i in key:
        r1 = f(Rhalf, i)
        r1 = XOR(Lhalf, r1)
        Lhalf = Rhalf
        Rhalf = r1
    Lhalf,Rhalf = Rhalf,Lhalf
    return Lhalf+Rhalf

# Decryption function Feistel Cipher
def decrypt(cipher, key):
    key = key[::-1]
    return encrypt(cipher, key)

# N time Encryption function Feistel Cipher
def n_Feistel_encrypt(msg, key, n, showintermediate=False):
    for i in range(n):
        msg = encrypt(msg, key)
        if showintermediate:
            print(msg)
    print(msg)
    return msg

# N time Decryption function Feistel Cipher
def n_Feistel_decrypt(cipher, key, n, showintermediate=False):
    for i in range(n):
        cipher = decrypt(cipher, key)
        if showintermediate:
            print(cipher)
    print(cipher)
    return cipher

# Eg:
msg = "OrgMsg".upper()
key = [3,2]
cipher = n_Feistel_encrypt(msg, key, 5, showintermediate=True)
newmsg = n_Feistel_decrypt(cipher, key, 5, showintermediate=True)

if newmsg == msg:
    print("Success")