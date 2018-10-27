import encrypt

g = 2
prime = 7
m0 = "2"
m1 = "3"

def main():
    x = int(input("Enter private factor: "))
    X = pow(g, x, prime)
    print(X)
    Y = int(input("Enter public factor: "))
    key0 = str(pow(Y, x, prime)).encode("utf-8")
    key1 = str(pow(int(Y/X), x, prime)).encode("utf-8")
    key_hashed_0 = encrypt.getHash(key0)
    key_hashed_1 = encrypt.getHash(key1)
    cipher_0 = encrypt.cipher(key_hashed_0, m0)
    cipher_1 = encrypt.cipher(key_hashed_1, m1)
    print(str(cipher_0) + " " + str(cipher_1))

if __name__ == "__main__":
    main()