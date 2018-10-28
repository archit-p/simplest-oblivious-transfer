import encrypt
import codecs
import requests
import random
import json

def initiate():
    global g
    global prime
    global y
    #Send a request to the sender
    r = requests.get('http://0.0.0.0:8080')
    #Recieve the shared prime and generator
    g = int((r.json())['generator'])
    prime = int((r.json())['prime'])
    print('The prime recieved is ',prime)
    print('The generator recieved is',g,'\n')
    #Generating a private factor
    y = random.randint(2,100)
    print('The private factor to be used by the reciever is ',y,'\n')

def calchash():
    global X
    global bit
    global key
    global key_hashed
    global Y
    #Send a request to the sender
    r = requests.get('http://0.0.0.0:8080/priv')
    #Recieve the public exponent
    X = int((r.json())['public'])
    print('The recieved public exponent is ',X,'\n')
    #Choose the message option
    bit = int(input('Enter 0 or 1 to choose message\n'))
    #Calculate the public factor to be sent
    if(bit == 0):
        Y = pow(g, y, prime)
    else:
        Y = X*pow(g, y, prime)
    print("Public factor to send = " + str(Y),'\n')
    #Generate the key
    key = str(pow(X, y, prime)).encode("utf-8")
    #Obtain the hash of the generated key
    key_hashed = encrypt.getHash(key)
    print('Hash of Key calculated\n')


def final():
    #Send a request to the sender
    payload=json.dumps({'Public':Y})
    r = requests.get('http://0.0.0.0:8080/enc',data=payload)
    #Obtain the ciphers
    cipher_0 = (r.json())['cipher_0']
    cipher_1 = (r.json())['cipher_1']
    #Decrypt the messages using the obtained ciphers
    m_0 = encrypt.decipher(key_hashed, cipher_0)
    m_1 = encrypt.decipher(key_hashed, cipher_1)
    print('Decrypted version of message 1:',m_0)
    print('Decrypted version of message 2:',m_1,'\n')
    #Obtain the required message
    if(bit == 0):
        print('The chosen message was:',m_0)
    else:
        print('The chosen message was:',m_1)

if __name__ == "__main__":
    #Send the request to the sender to initiate oblivious transfer and obtain the common prime and generator
    initiate()
    #Choose the required message option and calculate the hash of the chosen message's key
    calchash()
    #Recieve the ciphers from the sender and obtain the required message
    final()
