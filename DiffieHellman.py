import threading
import time
from RabinMiller import genPrime
import random

def Alice():
    msg = "Alice starts the Key Exchange\n"
    print(msg)
    time.sleep(2)
    sharedPrime = genPrime(4)
    sharedModulo = random.randint(2,sharedPrime)
    print("Alice sends - \nPrime to be used ",sharedPrime," Modulo - ",sharedModulo,"\n")
    sharedData.append(sharedPrime)
    sharedData.append(sharedModulo)
    time.sleep(2)
    privateKey = random.randint(2,sharedPrime)
    msg = 'Alice calculates private key - '+str(privateKey)+'\n'
    print(msg)
    publicKey = pow(sharedData[0],privateKey,sharedData[1])
    msg = 'Alice calculates and shares Public Key - '+str(publicKey)+'\n'
    print(msg)
    sharedData.append(publicKey)
    time.sleep(2)
    while(len(sharedData) !=4):
        pass
    if sharedData[2] == publicKey:
        bobpub = sharedData[3]
    else :
        bobpub = sharedData[2]
    msg = 'Alice receives Bobs public key '+str(bobpub)+'\n'
    print(msg)
    sharedKey = pow(privateKey,bobpub,sharedData[1])
    msg = 'Alice calculates shared key '+str(sharedKey)+'\n'
    print(msg)


def Eve():
    msg = "Eve attempts to eavesdrop on the conversation\n"
    print(msg)
    time.sleep(2)
    while(len(sharedData) != 2):
        pass
    msg = 'Eve intercepts-\n'+str(sharedData[0])+' '+str(sharedData[1])+'\n'
    print(msg)
    time.sleep(2)
    while(len(sharedData) !=4):
        pass
    msg = 'Eve intercepts-\n'+str(sharedData[2])+' '+str(sharedData[3])+'\n'
    print(msg)
    time.sleep(2)

def Bob():
    msg = "Bob agrees to establish a shared secret\n"
    print(msg)
    time.sleep(2)
    while(len(sharedData) != 2):
        pass
    msg = 'Bob receives-\n'+str(sharedData[0])+' '+str(sharedData[1])+'\n'
    print(msg)
    time.sleep(2)
    privateKey = random.randint(2,sharedData[0])
    msg = 'Bob calculates private key - '+str(privateKey)+'\n'
    print(msg)
    publicKey = pow(sharedData[0],privateKey,sharedData[1])
    msg = 'Bob calculates and shares Public Key - '+str(publicKey)+'\n'
    print(msg)
    sharedData.append(publicKey)
    time.sleep(2)
    while(len(sharedData) !=4):
        pass
    if sharedData[2] == publicKey:
        bobpub = sharedData[3]
    else :
        bobpub = sharedData[2]
    msg = 'Bob receives Alices public key '+str(bobpub)+'\n'
    print(msg)
    sharedKey = pow(privateKey,bobpub,sharedData[1])
    msg = 'Bob calculates shared key '+str(sharedKey)+'\n'
    print(msg)




sharedData=[]
p1 = threading.Thread(target = Alice)
p2 = threading.Thread(target = Bob)

p1.start()
p2.start()

Eve()
p1.join()
p2.join()
print('Eve cannot obtain the shared key')
