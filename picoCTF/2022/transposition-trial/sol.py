with open("message.txt", "r") as f:
	c = f.read()

blocks = [c[i:i+3] for i in range(0, len(c), 3)]
transposed_blocks = [b[2] + b[0] + b[1] for b in blocks]

print("".join(transposed_blocks))

