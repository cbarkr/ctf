with open("values", "r") as f:
	_, c, n, e = f.readlines()
	c = int(c[3:])
	n = int(n[3:])
	e = int(e[3:])

# n factored using FactorDB
# See https://factordb.com/index.php?query=1422450808944701344261903748621562998784243662042303391362692043823716783771691667
p = 2159947535959146091116171018558446546179
q = 658558036833541874645521278345168572231473

phi = (p-1) * (q-1)
d = pow(e, -1, phi)

m = pow(c, d, n)
m_bytes = bytes.fromhex(hex(m)[2:])
m_str = m_bytes.decode("utf-8")

print(m_str)
