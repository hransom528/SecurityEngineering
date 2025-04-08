# Harris Ransom
# Security Engineering Lab 2
# Part 6: Secure Key Exchange using Diffie-Hellman

# Imports
import secrets
import sympy
import random

# Generate a random prime number between a lower and upper bound
# See: https://stackoverflow.com/questions/21043075/generating-large-prime-numbers-in-python
def rand_prime(bits):
    while True:
        p = secrets.randbits(bits)
        if (sympy.isprime(p)):
            break
    return p

# MAIN
if __name__ == "__main__":
    # Generate large prime number
    p = rand_prime(256)

    # Secret values
    a = random.randrange(3, 101+1, 2)
    b = random.randrange(2, 100+1, 2)

    # Generator
    g = 2 

    # Modular exponentiation
    A = pow(g, a) % p
    B = pow(g, b) % p

    # Shared secret
    secretA = pow(B, a) % p
    secretB = pow(A, b) % p
    if (secretA == secretB):
        print("Shared secret established successfully!")
        print("Shared secret: ", secretA)
    else:
        print("Shared secret establishment failed!")
    print("Alice's secret: ", a)
    print("Bob's secret: ", b)
    
