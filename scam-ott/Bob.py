import random
import os

print('Awaiting contact from Alice\n')
f = open('shared.txt', 'r+', os.O_NONBLOCK)
n = 10
z = ''
while n!=0:
    n = n-1
    k = f.read(5)
    print(k)
    
    if str(k) == str('Alice'):
        print('Contact from Alice')
