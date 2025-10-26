# The key is literally given to us
MAPPED = {
    "Z": "A",
    "G": "B",
    "S": "C",
    "O": "D",
    "C": "E",
    "X": "F",
    "P": "G",
    "Q": "H",
    "U": "I",
    "Y": "J",
    "H": "K",
    "M": "L",
    "I": "M",
    "L": "N",
    "E": "O",
    "R": "P",
    "V": "Q",
    "T": "R",
    "B": "S",
    "W": "T",
    "N": "U",
    "A": "V",
    "F": "W",
    "J": "X",
    "D": "Y",
    "K": "Z",
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