import hashlib
import re

block_size = 16


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def decrypt(ciphertext, key):
    plaintext = b''
    key_hash = hashlib.sha256(key).digest()

    for i in range(0, len(ciphertext), block_size):
        # NOTE: Each block encrypted using the same part of the key
        block = ciphertext[i:i + block_size]
        plain_block = xor_bytes(block, key_hash)
        plaintext += plain_block

    return plaintext


def main():
    with open("enc_flag", "r") as f:
        key, c = f.readlines()

    key = eval(key[5:])
    c = eval(c[22:])

    decrypted_blockchain = decrypt(c, key)

    # The flag is the token in the middle of the plaintext!
    flag = re.search(b'picoCTF{.*}', decrypted_blockchain)
    print(flag.group(0).decode("utf-8"))


if __name__ == "__main__":
    main()
