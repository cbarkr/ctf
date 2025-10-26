# This time, the mapping was iteratively constructed based on likely words in the ciphertext
# E.g. "The", "be", "to", "of", "picoCTF", etc.
MAPPED = {
    "Y": "T",
    "A": "H",
    "R": "E",
    "T": "F",
    "H": "L",
    "J": "A",
    "M": "G",
    "Z": "I",
    "E": "S",
    "B": "P",
    "I": "I",
    "S": "C",
    "K": "O",
    "D": "R",
    "N": "U",
    "O": "Y",
    "X": "M",
    "C": "N",
    "Q": "D",
    "G": "W",
    "L": "B",
    "W": "V",
    "V": "K",
    "U": "Q"
}

with open("message.txt", "r") as f:
    c = f.read()

subbed = ""

for char in c:
    # Gets substitution from mapping
    # Returns the original character if it is not in the map
    sub = MAPPED.get(char.upper(), char)
    subbed += sub.lower() if char.islower() else sub

if "picoCTF" in subbed:
    idx = subbed.find("picoCTF")
    print(subbed[idx:])