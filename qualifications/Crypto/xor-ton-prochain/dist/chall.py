FLAG = "NBCTF{CENSURÉ}".encode("utf-8")
assert FLAG.startswith(b"NBCTF{") and FLAG.endswith(b"}")

def xor_ton_prochain(pt):
	ct = []
	for i,v in enumerate(pt):
		ct.append(v ^ pt[(i+1) % len(pt)])
	return bytes(ct)

out = xor_ton_prochain(FLAG)
open("output.txt", "w") \
	.write(f"ct = bytes.fromhex('{out.hex()}')")