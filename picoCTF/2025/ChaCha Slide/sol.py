m1 = b"Did you know that ChaCha20-Poly1305 is an authenticated encryption algorithm?"
e1 = bytes.fromhex("028dae4777beee769d7e37cf5bf8081fcaecaa21ec9a4daedc59d5e7410dd985f1f9ca1a5caa6d611f5a493d3af057d59ef73c9888325f915aa8bc786f2d00a54b850382c694638aef524f1c328a79eef0b7497d71eb810949906e94f5511ba9de0a2aa48358a266ed")
c1 = e1[:-28]
t1 = e1[-28:-12]
n1 = e1[-12:]
ad1 = b""

m2 = b"That means it protects both the confidentiality and integrity of data!"
e2 = bytes.fromhex("128cab132ebcfe37986378d10fac100cd1b88c2af9aa05ad811d90975a09c594a1a6915c5cbd286e0513492427ec4b9b8bf03bd995394fd458b4b67e6f7d1baa048f4297cbd220f8985b1461025143e6800a2c0ee8db511ba9de0a2aa48358a266ed")
c2 = e2[:-28]
t2 = e2[-28:-12]
n2 = e2[-12:]
ad2 = b""

assert n1 == n2

m3 = b"But it's only secure if used correctly!"
ad3 = b""

from chacha_poly1305_forgery import chachapoly1305_forgery_attack

res = chachapoly1305_forgery_attack(
	ad1,
	c1,
	t1,
	ad2,
	c2,
	t2,
	m1,
	m3,
	ad3
)

for i in res:
	c3, t3 = i

	print(c3.hex() + t3.hex() + n1.hex())
