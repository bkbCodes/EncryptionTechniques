def f(msg, key):
    out = ""
    for i in msg:
        out += chr((ord(i)-ord('A')+key)%26+ord('A'))
    return out


def XOR(m1,m2):
    out = ""
    for i in range(len(m1)):
        n1 = ord(m1[i]) - ord("A")
        n2 = ord(m2[i]) - ord("A")
        out += chr(ord("A") + (n1^n2))
    return out

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


def decrypt(cipher, key):
    key = key[::-1]
    return encrypt(cipher, key)


def n_Feistel_encrypt(msg,key,n):
    for i in range(n):
        msg = encrypt(msg, key)
    print(msg)
    return msg

def n_Feistel_decrypt(cipher,key,n):
    for i in range(n):
        cipher = decrypt(cipher, key)
    print(cipher)
    return cipher


msg = "OrgMsg".upper()
key = [3,2]
cipher = n_Feistel_encrypt(msg, key, 5)
newmsg = n_Feistel_decrypt(cipher, key, 5)

if newmsg == msg:
    print("Success")