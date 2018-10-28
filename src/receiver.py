import encrypt
import codecs
import requests
import random
import json

def main():
    y = input("Enter private part: ")
    X = input("Enter public part: ")
    y = int(y)
    X = int(X)
    if(bit == 0):
        Y = pow(g, y, prime)
    else:
        Y = X*pow(g, y, prime)
    print("Public part to send = " + str(Y))
    key = str(pow(X, y, prime)).encode("utf-8")
    key_hashed = encrypt.getHash(key)
    cipher_0 = input("Cipher 0: ")
    cipher_1 = input("Cipher 1: ")
    m_0 = encrypt.decipher(key_hashed, cipher_0)
    m_1 = encrypt.decipher(key_hashed, cipher_1)
    print(m_0)
    print(m_1)

if __name__ == "__main__":
    r = requests.get('http://0.0.0.0:8080')
    g = int((r.json())['generator'])
    prime = int((r.json())['prime'])
    print('The prime recieved is ',prime)
    print('The generator recieved is',g)
    y = random.randint(2,100)
    print('The private factor to be used by the reciever is ',y)
    r = requests.get('http://0.0.0.0:8080/priv')
    X = int((r.json())['public'])
    print('The recieved public exponent is ',X)
    bit = int(input('Enter 0 or 1 to choose message\n'))
    if(bit == 0):
        Y = pow(g, y, prime)
    else:
        Y = X*pow(g, y, prime)
    print("Public factor to send = " + str(Y))
    key = str(pow(X, y, prime)).encode("utf-8")
    key_hashed = encrypt.getHash(key)
    print('Hash of Key calculated')
    payload=json.dumps({'Public':Y})
    r = requests.get('http://0.0.0.0:8080/enc',data=payload)
