import codecs
import hashlib

def getHash(val):
    m = hashlib.md5()
    m.update(val)
    return m.hexdigest()

def axorb(a, b):
    if(len(a) > len(b)):
        return bytes([x ^ y for (x, y) in zip(a[:len(b)], b)])
    else:
        return bytes([x ^ y for (x, y) in zip(a, b[:len(a)])])

def cipher(key, message):
    message = message.encode('utf-8')
    message = str(message.hex())
    while(len(message) < len(key)):
        message = message + "0"
    byte_key = codecs.decode(key, "hex")
    byte_message = codecs.decode(message, "hex")
    ct = axorb(byte_key, byte_message)
    return codecs.encode(ct, "hex")

def decipher(key, message):
    if(len(key) != len(message)):
        print(len(key))
        print(len(message))
        print("Sorry lengths don't match")
        return
    byte_key = codecs.decode(key, "hex")
    #print(byte_key)
    byte_message = codecs.decode(message, "hex")
    #print(byte_message)
    pt = axorb(byte_key, byte_message)
    pt = str(codecs.encode(pt, "hex"))[2:-1]
    while(pt[-1] == "0"):
        pt = pt[0:-1]
    pt = codecs.decode(pt,"hex")
    pt = pt.decode("utf-8",errors='ignore')
    return pt
