from RabinMiller import genPrime
from prim import primRoots
import random
import os

print('Alice attempts to start the key exchange')
sharedPrime = genPrime(1024)
print('The prime number to be utilized by Alice is',+sharedPrime,'\n')
prim = primRoots(sharedPrime)
print('The primitive root to be used is',+prim,'\n')
print('Attempting to contact Bob\n')
f = open('shared.txt', 'w+', os.O_NONBLOCK)
f.write('Alice')
