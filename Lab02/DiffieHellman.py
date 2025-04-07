# Harris Ransom
# Security Engineering Lab 2
# Part 6: Secure Key Exchange using Diffie-Hellman

# Imports
import math
import random

# MAIN
if __name__ == "__main__":
    # TODO: Large prime number
    #p = 

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
    else:
        print("Shared secret establishment failed!")
    print("Alice's secret: ", a)
    print("Bob's secret: ", b)
