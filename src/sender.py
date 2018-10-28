import encrypt
import random
from flask import Flask,jsonify,request
import requests
from RabinMiller import genPrime,primRoots
import json
import ast
import logging

#Setting up the server
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)


#Handle initial request
@app.route('/')
def main():
    global prime
    global g
    #Generate the shared prime and generator
    prime = genPrime(40)
    print("The generated prime is ",prime)
    g = random.randint(2,100)
    print("The generator to be used is ",g,'\n')
    #Share the prime and generator
    return jsonify({'prime':prime,'generator':g})

#Handle calchash request
@app.route('/priv')
def priv():
    global x
    global X
    #Calculate the private factor
    x = random.randint(2,100)
    print('The private factor to be used by sender is ',x,'\n')
    X = pow(g, x, prime)
    #Calculate and return the public exponent
    print('The public exponent is ',X,'\n')
    return jsonify({'public':X})

#Handle the final request
@app.route('/enc',methods=['GET'])
def enc():
    global Y
    data = ast.literal_eval((request.data).decode('utf-8'))
    #Obtain the public factor
    Y = int(data['Public'])
    print('Recieved public factor is ',Y,'\n')
    #Calculate and create the hash of the two keys
    key0 = str(pow(Y, x, prime)).encode("utf-8")
    key1 = str(pow(int(Y/X), x, prime)).encode("utf-8")
    key_hashed_0 = encrypt.getHash(key0)
    print('Hash of Key 1 calculated')
    key_hashed_1 = encrypt.getHash(key1)
    print('Hash of Key 2 calculated\n')
    #Encrypt both the messages and return to the reciever
    cipher_0 = encrypt.cipher(key_hashed_0, m0)
    print('Cipher of message 1 calculated')
    cipher_1 = encrypt.cipher(key_hashed_1, m1)
    print('Cipher of message 2 calculated\n')
    print('Waiting for receiver\n')
    return jsonify({'cipher_0':cipher_0.decode("utf-8"),'cipher_1':cipher_1.decode("utf-8")})

if __name__ == "__main__":
    #Input the messages to be sent
    m0 = str(input('Enter the first message to be sent\n'))
    m1 = str(input('Enter the second message to be sent\n'))
    print('Waiting for receiver\n')
    #Start the server
    app.run(host='0.0.0.0',port=8080)
