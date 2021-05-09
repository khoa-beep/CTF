with open('E:\Hacking\RE\CTF\DawgCTF\sections','rb') as byte_reader:
    p = byte_reader.read()
p_xor = ""
for i in p:
    p_xor += chr(i^0x78)

with open('output','wb') as wb:
    wb.write(p_xor.encode())
