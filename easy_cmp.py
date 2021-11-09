flag_enc = '********CENSORED********'
m = [0x410A4335494A0942, 0x0B0EF2F50BE619F0, 0x4F0A3A064A35282B]

import binascii
flag = b''
for i in range(3):
    p = flag_enc[i*8:(i+1)*8] # tach chuoi ra
     #********
 #    CENSORED      
     #********  
    print(p)
    a = binascii.b2a_hex(p.encode('ascii')[::-1]) # chuyen chuoi ve ascii dao nguoc
    print(a)
    b = binascii.a2b_hex(hex(int(a,16) + m[i])[2:])[::-1]
    print(b)
    print('\n')

    flag += b
print(flag)