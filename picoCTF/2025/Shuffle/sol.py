with open("output.txt", "r") as f:
	c = f.read()

flag = ""

c = c[::-1]

for i in range(0, len(c), 3):
	flag += c[i+1]
	flag += c[i+2]
	flag += c[i]

print(flag)
