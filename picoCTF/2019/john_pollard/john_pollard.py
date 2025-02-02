from gmpy2 import iroot

def find_p(n):
	sqrtn = iroot(n, 2)[0]
	cbrtn = iroot(n, 3)[0]

	for i in range(sqrtn, cbrtn, -2):
		if n % i == 0:
			return i

if __name__ == "__main__":
	n = 4966306421059967
	p = find_p(n)
	q = int(n/p)
	res = "picoCTF" + "{" + f"{q}" + "," + f"{p}" + "}"
	print(res)
