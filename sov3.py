import base64

key = "e3nifIH9b_C@n@dH"
de_c = ''
flag = ''
for i in range(0,len(key)):
    de_c += chr(ord(key[i]) - i)
flag = base64.b64decode(de_c)
flag = flag.decode('ASCII')
print(flag)