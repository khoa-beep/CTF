username = [0]*7 
password = [0]*5 
username[0] = 57 ^ 114 
username[1] = 127 - username[0] 
username[2] = 182 - username[0] 
username[3] = username[2] - 10 
username[4] = 82 
username[5] = username[4] - 34 
username[6] = 100 + 16 
password[0] = 54 + 0x11 
password[1] = 119 ^ password[0] 
password[2] = 124 ^ 23 
password[3] = 103 + 14 
password[4] = 192 - password[2] 
print(''.join([chr(i) for i in username]))
print(''.join([chr(i) for i in password]))