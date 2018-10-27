import encrypt

bit = 0
g = 2
prime = 7

def main():
    y = input("Enter private part: ")
    X = input("Enter public part: ")
    y = int(y)
    X = int(X)
    Y = 0
    if(bit == 0):
        Y = pow(g, y, prime)
    else: 
        Y = X*pow(g, y, prime)
    print("Public part to send = " + str(Y))
    key = str(pow(Y, x, prime)).encode("utf-8")
    key_hashed = encrypt.getHash(key)
    cipher_0 = input("Enter cipher 0 = ")
    cipher_1 = input("Enter cipher 1 = ")
    m_0 = encrypt.decipher(key, cipher_0)
    m_1 = encrypt.decipher(key, cipher_1)
    print(m_0)
    print(m_1)

if __name__ == "__main__":
    main()