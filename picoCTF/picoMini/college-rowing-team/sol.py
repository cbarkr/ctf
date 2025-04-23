from gmpy2 import iroot


def small_e(c_list):
	e = 3

	for c in c_list:
		m, is_valid = iroot(c, e)

		if is_valid:
			m_bytes = m.to_bytes(len(str(m)), "big").strip(b"\x00")

			if b"picoCTF" in m_bytes:
				print(m_bytes)
				break


def main():
	c_list = []

	with open("encrypted-messages.txt", "r") as f:
		for line in f.readlines():
			if line.startswith("c: "):
				c_list.append(int(line[3:]))

	small_e(c_list)


if __name__ == "__main__":
	main()
