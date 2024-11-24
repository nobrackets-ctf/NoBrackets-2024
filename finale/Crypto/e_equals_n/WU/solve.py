from Crypto.Util.number import long_to_bytes

exec(open("output.txt", "r").read())

φ = N - e
d = pow(e, -1, φ)
m = pow(c,  d, N)

print(long_to_bytes(m).decode("utf-8"))