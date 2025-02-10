with open("chall.txt", "rb") as f:
	c = f.read().decode("iso8859-1")

flag = ""

for i in c:
	binstring = bin(ord(i))[2:]

	for j in range(len(binstring)):
		if binstring[j] == "0":
			binstring = binstring[:j-1] + binstring[j:]
			break

	flag += chr(int(binstring, 2))

print(flag)
