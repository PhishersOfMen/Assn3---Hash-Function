msg = input()

h0 = 0x68619501
h1 = 0xEF352189
h2 = 0x9ADBACFE

ml = list(''.join(format(8 * len(msg), 'b')))
while len(ml) < 64:
    ml.insert(0, '0')

bin_msg = list(''.join(format(ord(i), 'b') for i in msg))

bin_msg.append('1')
while (len(bin_msg) % 512) != 448:
    bin_msg.append('0')

for c in ml:
    bin_msg.append(c)

for i in range(0, len(bin_msg), 512):
    chunk = bin_msg[i:i+512]

    for i in range(0, len(chunk), 32):
        w = chunk[i:i+32]

        for i in range(16, 47):
            w.append(str(((int(w[i-3]) ^ int(w[i-8]) ^ int(w[i-14]) ^ int(w[i-16])) << 1) & 1))

        a = h0
        b = h1
        c = h2

        for i in range(0, 48):
            if 0 <= i and i <= 11:
                f = (b|~c)|(b&~c)
                k = 0x568CAEFA
            elif 12 <= i and i <= 23:
                f = (~c|(b&c))^(b|c)
                k = 0x8D1629B2
            elif 24 <= i and i <= 35:
                f = (b|~c)^c
                k = 0x0F2439FF
            else:
                f = b^c
                k = 0xBADBADFF
            
            temp = ((a << 5) + f + k + int(w[i]))
            a = c & 0xFFFFFFFF
            c = (b << 7) & 0xFFFFFFFF
            b = temp & 0xFFFFFFFF

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF

hh = (h0 << 64) | (h1 << 32) | h2

print (hex(hh))