# Obscure - Reversing

Ta tải file thử thách và phân tích.

khoa@DESKTOP-L14K8T1:/mnt/c/Users/DELL/Downloads/obscure$ file reverseme.pyc 

reverseme.pyc: python 2.7 byte-compiled

Đây là file được biên dịch từ chương trình python ( nó như file .exe vậy )

ta sẽ sử dụng lệnh : uncompyle6 -o . reverseme.pyc

để biên dịch ra mã nguồn.

Vào mã nguồn python phân tích.

```python
# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
# [GCC 9.3.0]
# Embedded file name: reverseme.py
# Compiled at: 2021-09-04 16:21:21
import numpy as np
flag = 'TamilCTF{this_one_is_a_liability_dont_fall_for_it}'
np.random.seed(369)
data = np.array([ ord(c) for c in flag ])
extra = np.random.randint(1, 5, len(flag))
product = np.multiply(data, extra)
temp1 = [ x for x in data ]
temp2 = [ ord(x) for x in 'dondaVSclb' * 5 ]
c = [ temp1[i] ^ temp2[i] for i in range(len(temp1)) ]
flagdata = ('').join(hex(x)[2:].zfill(2) for x in c)
real_flag = '300e030d0d1507251700361a3a0127662120093d551c311029330c53022e1d3028541315363c5e3d063d0b250a090c52021f'
```

Câu này nó cho 1 flag thực và flag fake mà phía trên nó làm nhưng gì đó để mã hóa cờ ta , mình nghĩ nó sẽ làm xáo trộn cờ .

Hint: ta sẽ đảo ngược nó lại bằng cách viết lại hàm trên và cuỗi cùng là cho chuỗi read flag thỏa mãn điều kiện.

My scritp

```python
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

```

**flag **: TamilCTF{bRuTeF0rCe\_1s_tHe\_0nLy_F0rCe\_2\_bReAk\_\_1n}
