import itertools

def unscramble(L):
    A = L

    for a in A:
        for idx, elem in enumerate(a):
            if isinstance(elem, list):
                a.pop(idx)

    return list(itertools.chain.from_iterable(A))


def get_flag(hex_flag):
    flag = ""

    for i in hex_flag:
        curr = int(i, 16)
        flag += chr(curr)

    return flag


def main():
    with open("enc_flag", "r") as f:
        c = eval(f.read())

    unscrambled = unscramble(c)
    flag = get_flag(unscrambled)
    print(flag)


if __name__ == "__main__":
    main()
