from hashlib import sha256

# Borrowed from `keygenme-trial.py`
bUsername_trial = b"SCHOFIELD"
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"

# Adapted from `check_key`
h = sha256(bUsername_trial).hexdigest()
key = h[4] + h[5] + h[3] + h[6] + h[2] + h[7] + h[1] + h[8]

print(f"{key_part_static1_trial}{key}{key_part_static2_trial}")
