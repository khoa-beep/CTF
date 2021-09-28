# rev/babyrev

#### About the task <a id="about-the-task-1"></a>

**Task description:** _well uh… this is what you get when you make your web guy make a rev chall._

{% file src="../../.gitbook/assets/babyrev.rar" caption="File dowload" %}

![](../../.gitbook/assets/image%20%2831%29.png)

Phân tích bằng Ghidra.

Phân tích kỹ hơn chút

![](../../.gitbook/assets/image%20%2839%29.png)

Ta để ý 2 hàm là memset và hàm rot\_n.

memset nó sẽ check từng byte trên và đem đi xor với 0x42 . 

Kết quả khi xor đây mình sử dụng cyber cheft 

![](../../.gitbook/assets/image%20%2838%29.png)

Ok ta đã có check cần rồi giờ ta vô xem hàm rot\_n \( hàm xoay \).

![](../../.gitbook/assets/image%20%2837%29.png)

Sau đó ta đã có đủ thông tin cần tìm rồi.

Ta sẽ kết hơp hàm nguyên tố + hàm xoay + với 2 điều kiện cuối của Rot\_n

Mã python ta sẽ được sau.

```python
import sympy
import string

check = [0x75,0x6a,0x70,0x3f,0x5f,0x6f,0x48,0x79,0x5f,0x6c,0x78,0x69,0x75,0x5f,0x7a,0x78,0x5f,0x75,0x76,0x65]

#check = [0x41,0x42,0x43]
# chyen thanh in thuog
ascii_lower = string.ascii_lowercase
# in hoa
ascii_upper = string.ascii_uppercase


for n in range(len(check)):
    bNum = n * 4 # n << 2
    while(True):
        # dung sympy de kiem tra snt
        if sympy.isprime(bNum):
            #print(bNum,end=",")
            break
        bNum += 1
    charToPrint = check[n]
    if(64 < check[n] < 91):
        charToPrint = ord(ascii_upper[((check[n] - 65) - bNum) % 26])
    if(96 < check[n] < 123):
        charToPrint = ord(ascii_lower[((check[n] - 97) - bNum) % 26])
    print(chr(charToPrint),end="")

```

Flag : 

```text
corctf{see?_rEv_aint_so_bad}
```



