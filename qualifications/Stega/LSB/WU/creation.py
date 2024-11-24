import wave
import random


cover_wav = wave.open("chall.wav", mode='rb')
frames = bytearray(cover_wav.readframes(cover_wav.getnframes()))

message_bits = []
for l in "NBCTF{D0_nOt_m3lt_th3_L5B}      CREDITS : VINCE HAWK & NAMINÉ - RIGHT HERE (Fm)":
    message_bits += [ (ord(l)>>i)&1 for i in range(8) ]
    
j = 0
for i in range(3000000, len(frames), 3):
    if frames[i]%2 != message_bits[j]:
        if frames[i] == 255:
            s = -1
        elif frames[i] == 0:
            s = +1
        else:
            s = random.choice([-1, +1])
        frames[i] = frames[i] + s
    j += 1
    if j>=len(message_bits):
        break

stego_wav = wave.open('chall.wav', 'wb')
stego_wav.setparams(cover_wav.getparams())
stego_wav.writeframes(bytes(frames))

cover_wav.close()
stego_wav.close()
