from pwn import *
from gmpy2 import gcd, invert


hostname = ...
port = ...


def main():
	e = 65537
	items = []

	for i in range(2):
		conn = remote(hostname, port)
		n = conn.recvline()
		conn.recvline()
		c = conn.recvline()

		n = int(n[2:])
		c = int(c[12:])

		items.append((n, c))

		conn.close()

	(n1, c1), (n2, c2) = items

	p1 = gcd(n1, n2)

	if p1 != 1:
		q1 = n1 // p1
		phi1 = (p1-1) * (q1-1)
		d1 = invert(e, phi1)
		m1 = pow(c1, d1, n1)

		m1_bytes = bytes.fromhex(hex(m1)[2:])
		m1_str = m1_bytes.decode("utf-8")

		print(m1_str)


if __name__ == "__main__":
	main()
