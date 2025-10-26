# The mapping was iteratively constructed based on likely words in the ciphertext
MAPPED = {
    "N": "T",
    "A": "H",
    "F": "E",
    "V": "F",
    "P": "L",
    "T": "A",
    "R": "G",
    "X": "I",
    "E": "S",
    "S": "P",
    "Z": "C",
    "Q": "O",
    "L": "N",
    "G": "M",
    "C": "K",
    "W": "U",
    "K": "B",
    "B": "D",
    "Y": "R",
    "H": "Y",
    "O": "X", 
    "U": "V", 
    "M": "W"
}

def get_freq_mapping(ciphertext: str) -> dict[str, str]:
    # Source: https://en.wikipedia.org/wiki/Letter_frequency
    FREQ = {
        "E": 12.7,
        "T": 9.1,
        "A": 8.2,
        "O": 7.5,
        "I": 7.0,
        "N": 6.7,
        "S": 6.3,
        "H": 6.1,
        "R": 6.0,
        "D": 4.3,
        "L": 4.0,
        "C": 2.8,
        "U": 2.8,
        "M": 2.4,
        "W": 2.4,
        "F": 2.2,
        "G": 2.0,
        "Y": 2.0,
        "P": 1.9,
        "B": 1.5,
        "V": 0.98,
        "K": 0.77,
        "J": 0.15,
        "X": 0.15,
        "Q": 0.095,
        "Z": 0.074,
    }

    import re
    from collections import Counter

    clean = re.sub(r"[^a-zA-Z]", "", c)
    count = Counter(clean.upper())
    freqs = { k: ((v/len(c)) * 100) for k, v in count.items() }

    sorted_eng = {k: v for k, v in sorted(FREQ.items(), key=lambda item: item[1], reverse=True)}
    sorted_msg = {k: v for k, v in sorted(freqs.items(), key=lambda item: item[1], reverse=True)}

    mapped = { k[0]: v[0] for k, v in zip(sorted_msg, sorted_eng)}

with open("message.txt", "r") as f:
    c = f.read()

# This was used to guide the process
# mapped = get_freq_mapping(c)

subbed = ""

for char in c:
    # Get substitution from manual mapping
    sub = MAPPED.get(char.upper(), char)

    # If not mapped, get from frequency analysis map
    # Otherwise, use the original character
    # if not sub:
    #     sub = mapped.get(char.upper(), char)

    subbed += sub.lower() if char.islower() else sub

if "picoCTF" in subbed:
    idx = subbed.find("picoCTF")
    print(subbed[idx:])