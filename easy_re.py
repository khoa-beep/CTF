# chuyen thap phan ve ky tu
arr_new = [0x40, 0x35, 0x20, 0x56, 0x5D, 0x18, 0x22, 0x45, 0x17, 0x2F, 
  0x24, 0x6E, 0x62, 0x3C, 0x27, 0x54, 0x48, 0x6C, 0x24, 0x6E, 
  0x72, 0x3C, 0x32, 0x45, 0x5B, 0x00]
result = 'flag'
key = []

for i in range(4):
   key.append(arr_new[i] ^ ord(result[i]))

for i in range(25):
    print(chr(arr_new[i] ^ key[i % 4]),end='')