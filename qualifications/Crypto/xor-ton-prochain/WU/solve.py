exec(open("output.txt").read())

pt = [None for _ in range(len(ct))]
pt[0] = ord("N")

for i in range(len(ct) - 1):
	pt[i+1] = pt[i] ^ ct[i]

print(bytes(pt))