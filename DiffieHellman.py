import threading
from RabinMiller import genPrime

def Alice():
    print("Alice starting the Key Exchange")
    prime = genPrime(40000)
    print("Alice\nPrime to be used ",prime," \n")

def Bob():
    print("Bob agrees to establish a shared secret")

def Eve():
    print("Eve attempting to eavesdrop on the conversation")


p1 = threading.Thread(target = Alice)
p2 = threading.Thread(target = Bob)
p3 = threading.Thread(target = Eve)

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()
