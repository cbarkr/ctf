with open("enc", "r") as f:
	c = f.read()

flag = ''.join([chr(ord(c[i]) >> 8) + (chr(ord(c[i]) - (ord(chr(ord(c[i]) >> 8)) << 8))) for i in range(len(c))])

print(flag)
