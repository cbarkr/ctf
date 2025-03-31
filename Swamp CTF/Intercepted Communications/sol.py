c_list = []
m_list = []

for i in range(1, 6):
	with open(f"Captured_comms/M{i}/encrypted.txt") as f:
		c_list.append(int(f.read(), 2))

	with open(f"Captured_comms/M{i}/decrypted.txt") as f:
		m_list.append(int(f.read(), 2))

with open("Captured_comms/Important_Message_Captured.txt", "r") as f:
	c = int(f.read(), 2)

k_list = [m ^ c for m, c in zip(m_list, c_list)]
ttp_list = [c ^ k for k in k_list]

for ttp in ttp_list:
	print(ttp.to_bytes(len(str(ttp)), "big").strip(b"\x00"))

