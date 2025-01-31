from gmpy2 import iroot


with open("ciphertext", "r") as f:
	space1, n, e, space2, c = f.readlines()
	n = int(n[3:])
	e = int(e[3:])
	c = int(c[16:])


m, is_exact = iroot(c, e)
if is_exact and pow(m, e, n) == c:
	print(m.to_bytes(256, "big").decode("utf-8").strip("\x00").strip())
