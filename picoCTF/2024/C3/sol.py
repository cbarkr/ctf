lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

with open("ciphertext", "r") as f:
	c = f.read()

flag = ""

prev = 0
for i in c:
	cur_sub_prev_mod40 = lookup2.index(i)
	cur = (cur_sub_prev_mod40 + prev) % 40
	flag += lookup1[cur]
	prev = cur

print(flag)
