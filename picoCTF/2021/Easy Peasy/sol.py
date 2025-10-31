# The encrypted flag
c1 = 0x551e6c4c5e55644b56566d1b5100153d4004026a4b52066b4a5556383d4b0007

# After padding the input until the key wrapped around
# Encrypt a bunch of "a"'s (where bunch is the length of the flag)
# And get the corresponding ciphertext
m = 0x6161616161616161616161616161616161616161616161616161616161616161
c2 = 0x03463d1959523d1907513d190503163d1903543d1904573d1900003b3d190457

# C = M ^ K -> K = M ^ C
key = m ^ c2

# C = M ^ K -> M = C ^ K
flag = c1 ^ key
print(flag.to_bytes(32, "big"))
