from Crypto.Util.number import getPrime
from gmpy2 import gcd, next_prime

p = pow(2, 63)
while gcd(65537, p-1) == 1:
	p = next_prime(p)

print(f"p = {p}")
print(f"q = {getPrime(64)}")
