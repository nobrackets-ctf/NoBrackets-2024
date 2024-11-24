exec(open("output.txt", "r").read())
INGREDIENTS = ["🧈", "🧅", "🧄", "🥓", "🥩", "🥕", "🍷", "🍄", "🌿"]
NB_INGREDIENTS = len(INGREDIENTS)

# Conversion de out en base 10
base_10 = 0
for i,v in enumerate(out):
	v = INGREDIENTS.index(v)
	base_10 += v*NB_INGREDIENTS**i

# Conversion de base 10 en base 256
res = []
while base_10 > 0:
	res.append(base_10 % 256)
	base_10 //= 256

flag = bytes(res)
print(flag.decode("utf-8"))
