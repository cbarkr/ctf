import base64
from Crypto.Cipher import AES

# REF: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-gppref/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be
key_hex = "4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b"
key_bytes = bytes.fromhex(key_hex)

cpassword_b64 = "dAw7VQvfj9rs53A8t4PudTVf85Ca5cmC1Xjx6TpI/cS8WD4D8DXbKiWIZslihdJw3Rf+ijboX7FgLW7pF0K6x7dfhQ8gxLq34ENGjN8eTOI="
cpassword_decoded = base64.b64decode(cpassword_b64)

cipher = AES.new(key_bytes, AES.MODE_CBC)
flag = cipher.decrypt(cpassword_decoded)

print(flag.decode("utf-8", errors="ignore"))
