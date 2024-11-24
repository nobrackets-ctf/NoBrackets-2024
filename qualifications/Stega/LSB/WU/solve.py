import wave
cover_wav = wave.open("chall.wav", mode='rb')
frames = bytearray(cover_wav.readframes(cover_wav.getnframes()))
message_ex = []
value = 0
j = 0
for i in range(0, len(frames), 3):
    msg_bit = frames[i]%2
    if j%8==0 and j!=0:
        message_ex.append(value)
        value = 0
    value |= msg_bit << j%8
    j+=1
with open("flag", "w", encoding="utf-8") as f:
    f.write(str(''.join([chr(l) for l in message_ex])))
cover_wav.close()
