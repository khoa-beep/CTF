
import random
import string
import numpy as np
flag_read = '300e030d0d1507251700361a3a0127662120093d551c311029330c53022e1d3028541315363c5e3d063d0b250a090c52021f'


def encrypt(flag):
    np.random.seed(369) 
    data=np.array([ord(c) for c in flag]) 
    extra=np.random.randint(1,5,len(flag)) 
    product=np.multiply(data,extra) 
    temp1=[x for x in data] 
    temp2=[ord(x) for x in "dondaVSclb"*5] 
    c=[temp1[i]^temp2[i] for i in range(len(temp1))] 
    flagdata=''.join(hex(x)[2:].zfill(2) for x in c)
    return flagdata


flag = list('TamilCTF{')
while(True):
    for character in string.printable:
        out = encrypt(''.join(flag)+character)
        if flag_read.startswith(out):
            flag.append(character)
            print("Found one character "+"".join(flag))
        if flag_read == out:
            exit()
