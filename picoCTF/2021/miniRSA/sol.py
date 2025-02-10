from gmpy2 import iroot


with open("ciphertext", "r") as f:
	n, e, space, c = f.readlines()
	n = int(n[3:])
	e = int(e[3:])
	c = int(c[16:])


for i in range(4096):
	# Pad by a multiple of `n`
	padded, is_exact = iroot(c + (i * n), e)
	
	if is_exact and pow(padded, e, n) == c:
		print(padded.to_bytes(256, "big").decode("utf-8").strip("\x00").strip())
		break
