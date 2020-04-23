

from random import *
import gmpy2
from gmpy2 import mpz, powmod, is_prime
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
            return False
    return True

newLine = ""
newList = []
file1 = open("test_file.txt", "r")
numerator = 0
denominator = 10000
for num in range(10000):

    newLine = file1.readline()
    newList = newLine.split()


    #userInput = input("Number to be Tested:  ")
    #n = mpz(userInput)

    if (isPrime(mpz(newList[1]), 6) == is_prime(int(newList[1]))):
        numerator += 1
    else:
        print("TESTNUM = ", end = '')
        print(newList[1])
        print("My Test: ", end = '')
        print(isPrime(mpz(newList[1]), 6))
        print("Actual: ", end = '')
        print(is_prime(int(newList[1])))
        print("****************")

print((numerator/denominator) * 100, end = '')
print('%')
n = mpz(28765)
print("TESTNUM = ", end = '')
print(n)
print("My Test: ", end = '')
print(isPrime(mpz(n), 6))
print("Actual: ", end = '')
print(is_prime(int(n)))
print("****************")