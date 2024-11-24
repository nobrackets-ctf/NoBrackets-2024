"""
Sachant que chaque nombre d'indice `i` est strictement deux fois supérieur au nombre
d'indice `i-1`, on sait que la somme des n premiers nombres est inférieur au (n+1)-ième
nombre. NOTE: Tu peux faire un schéma avec des batons pour comprendre ça.

On en déduit alors que si la somme finale (i.e. le ciphertext) est plus grande que le
dernier nombre de la pk, c'est que le dernier nombre est compris dans cette somme, et donc
que le dernier bit du flag est a 1, on peut donc soustraire le plus grand nombre de la
somme et réitérer jusqu'à parcourir tous les nombres !
"""

exec(open("output.txt", "r").read())

def bin_to_bytes(b):
    return bytes.fromhex(hex(int(b, 2))[2:])

# Parce-que `pk` est une super-increasing sequence
def decrypt(Σ, pk):
    pt = ''
    for nb in pk[::-1]:
        if Σ >= nb:
            pt += '1'
            Σ  -= nb
        else:
            pt += '0'

    return pt[::-1]

pt = decrypt(ct, pk)
flag = bin_to_bytes(pt).decode('utf-8')
print(f"{flag = }")