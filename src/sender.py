import encrypt
import random
from flask import Flask,jsonify,request
import requests
from RabinMiller import genPrime,primRoots
import json
import ast

app = Flask(__name__)
m0 = str(input('Enter the first message to be sent\n'))
m1 = str(input('Enter the second message to be sent\n'))

@app.route('/')
def main():
    global prime
    global g
    prime = genPrime(40)
    print("The generated prime is ",prime)
    g = random.randint(2,100)
    print("The generator to be used is ",g)
    return jsonify({'prime':prime,'generator':g})


@app.route('/priv')
def priv():
    global x
    global X
    x = random.randint(2,100)
    print('The private factor to be used by sender is ',x)
    X = pow(g, x, prime)
    print('The public exponent is ',X)
    return jsonify({'public':X})


@app.route('/enc',methods=['GET'])
def enc():
    global Y
    data  = ast.literal_eval((request.data).decode('utf-8'))
    Y = int(data['Public'])
    print('Recieved public factor is ',Y)
    key0 = str(pow(Y, x, prime)).encode("utf-8")
    key1 = str(pow(int(Y/X), x, prime)).encode("utf-8")
    key_hashed_0 = encrypt.getHash(key0)
    print('Hash of Key 1 calculated')
    key_hashed_1 = encrypt.getHash(key1)
    print('Hash of Key 2 calculated')
    cipher_0 = encrypt.cipher(key_hashed_0, m0)
    print('Cipher of Key 1 calculated')
    cipher_1 = encrypt.cipher(key_hashed_1, m1)
    print('Cipher of Key 2 calculated')
    print(str(cipher_0) + " " + str(cipher_1))

if __name__ == "__main__":
    print('Waiting for receiver')
    app.run(host='0.0.0.0',port=8080)
