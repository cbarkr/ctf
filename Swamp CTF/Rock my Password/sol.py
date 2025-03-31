from hashlib import md5, sha256, sha512

# 1. Given the flag is from RockYou
with open("/usr/share/wordlists/rockyou.txt", "rb") as f:
        ry = f.read().splitlines()

# 2. Given that flag is 10 characters
shortlist = [i for i in ry if len(i) == 10]

with open("enc_flag", "r") as f:
	c = f.read().strip()

c_bytes = bytes.fromhex(c)

for guess in shortlist:
	# 3. Given that guess is hashed with the `swampCTF{}` text
	hashed_guess = b"swampCTF{" + guess.strip() + b"}"

	# 4. Given that the flag is hashed 100x with MD5
	for i in range(100):
		hashed_guess = md5(hashed_guess).digest()

	# 5. Then 100x with SHA256
	for i in range(100):
		hashed_guess = sha256(hashed_guess).digest()

	# 6. Then 100x with SHA512
	for i in range(100):
		hashed_guess = sha512(hashed_guess).digest()

	if hashed_guess == c_bytes:
		break

print(b"swampCTF{" + guess + b"}")
