#Name: Adam Sachsel
#Date: 04/22/2020
#Assn: RSN_Project
#Class: Marron CS441

import gmpy2
from gmpy2 import mpz, powmod, is_prime
from random import *

seed(123456789)

def primeGen(modSize):
    primeReturn = mpz(0)
    s = 50

    primeReturn = mpz(getrandbits(modSize/2))

    #Not even
    if (primeReturn % 2 == 0):
        primeReturn += 1
    
    #Miller-Rabin primality checking
    while (isPrime(primeReturn, s) != True):
        primeReturn += 2
    return primeReturn


#Input: a and b are integers you want the GCD of
#Output: d = GCD, x = 
def extEuclid(a, b):

    if (b == 0):
        return (a, 1, 0)
    else:

        (dPrime, xPrime, yPrime) = extEuclid(b, a % b)
        (d, x, y) = (dPrime, yPrime, xPrime - (a // b) * yPrime)
        return (d, x, y)
def isPrime(n, s):

    if n < 3:
        return True
    for num in range(s):
        a = mpz(randint(1, n-1))

        r = mpz((n-1))
        t = 0
        b = mpz(0)
        c = mpz(0)

        # Reduce r to ODD
        while (r % 2 == 0):
            r >>= 1
            t += 1

        b = (powmod(a, mpz(r), n))

        for i in range(t):

            c = powmod(b, 2, n)
            if (c == 1 and b != 1 and b != n-1):
                return False
            b = c
        if (c != 1):
            #Composite
            return False
    #Probably Prime        
    return True
    


def main():
    modSize = 0
    modSize = mpz(input("Please enter the desired bit size of the RSA Keys (Integer only):"))
    print("\n")
    message = input("Please enter string you wish to encrypt: ")
    
    #Primes Generated
    p = primeGen(modSize)
    q = primeGen(modSize)

    while (p == q):
        q = primeGen(modSize)
    
    n = p * q

    #Encryption Exponent
    e = (2 ** 16) + 1

    deltaN = (p-1)*(q-1)
    d = extEuclid(e, deltaN)[1]

    pubKey = [e, n]
    privKey = [d, n]


    x = 0
    for c in message:
        x = x << 8
        x = x ^ ord(c)
    print("Signature BEFORE encrypting with private key: ", end='')
    print(x, end='\n\n')


    #RSA ENCRYPTING
    encryptedMessage = int(pow(x, privKey[0], privKey[1]))
    print(encryptedMessage)

    #RSA DECRYPTING
    decryptedMessage = int(pow(encryptedMessage, pubKey[0], pubKey[1]))

    decryptedMessage = str(decryptedMessage)


    print ("String AFTER decrypting with public key: ", end = '')
    print (decryptedMessage, end= '\n\n')
    print ("Public Key [e, n]: ", end = '')
    print (pubKey, end= '\n\n')
    print ("Private Key [d, n]: ", end = '')
    print (privKey, end= '\n\n')







if __name__ == '__main__':
    main()