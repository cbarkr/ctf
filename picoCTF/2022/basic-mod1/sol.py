with open("message.txt", "r") as f:
	c = f.read()

flag = ""

upper_offset = 65
digit_offset = 22
__offset = 59

for i in c.split():
	char = int(i) % 37

	if char in range(0, 26):
		flag += chr(char + upper_offset)
	elif char in range(26, 36):
		flag += chr(char + digit_offset)
	else:
		flag += chr(char + __offset)

print(f"picoCTF{{{flag}}}")
