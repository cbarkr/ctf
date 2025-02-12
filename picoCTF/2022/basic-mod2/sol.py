from gmpy2 import invert

with open("message.txt", "r") as f:
	c = f.read()

flag = ""

upper_offset = 64
digit_offset = 21
__offset = 58

for i in c.split():
	char = int(i) % 41
	inv = invert(char, 41)

	if inv in range(1, 27):
		flag += chr(inv + upper_offset)
	elif inv in range(27, 37):
		flag += chr(inv + digit_offset)
	else:
		flag += chr(inv + __offset)

print(f"picoCTF{{{flag}}}")
