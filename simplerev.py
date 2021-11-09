key = list("ADSFKNDCLS".lower()) # convert danh sach sang thuong
text = "killshadow"
list_aphablet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Len_key = len(key)
flag = ''
for i in range(Len_key): # lap theo chuoi text
    str2 = text[i]
    for char in list_aphablet:  # lap theo danh sach
        if str2 == chr((ord(char) -39 - ord(key[i % Len_key]) + 97) % 26 + 97):
            flag += char
print('flag{{{}}}'.format(flag))

