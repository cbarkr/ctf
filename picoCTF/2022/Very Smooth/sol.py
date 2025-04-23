# REF: https://www.math.columbia.edu/~goldfeld/PollardAttack.pdf
# REF: https://ir0nstone.gitbook.io/crypto/rsa/factorisation-methods/pollards-p-1

from gmpy2 import gcd

with open("output.txt", "r") as f:
	n, c = f.readlines()

n = int(n[4:], 16)
c = int(c[4:], 16)

a = 2
curr = pow(a, 1)

for k in range(n//2):
	curr = pow(curr, k)
	p = gcd(curr-1, n)

	if p > 1:
		print("breaking!")
		break

print(p)
