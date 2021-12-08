# CTF wargames Pwn Kr 2

* **Category:** PWN
* **Points:** 3

## Challenge

collision

## Solution

Daddy told me about cool MD5 hash collision today. I wanna do something like that too!

```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
```

### Phân tích đề

```c
     if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
```

Trong main ta có thể thấy hàm main lấy tham số argc và so sanh nhỏ hơn 2 có nghĩa là nếu số lượng tham số không có lớn hơn 2 sẽ ret 0 và dừng ct.

```c
 if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }
```

Một câu lệnh dùng để so sánh sô lượng đầu vào của argv mà ở trong strlen vậy chắc là dùng cho độ dài là 20 ký tự .

Nếu không là in ra "passcode length ...."

```c
if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
```

Lại thêm 1 câu so sánh chắc đây so sánh hashcode (được khai báo toàn cục) có bằng với hàm check ko , ta xem bên trong nó là gì.

```c
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}
```

Hàm check pass , nhìn như tham số của ta được chuyển sang số nguyên và đem đi tính tổng vậy . Sau thì trả về trong res.

Khi kết quả thõa mãn thì ta sẽ nhảy vào win, mà vấn đề ở đây là cái mã hexcode kia nó lại không thõa mãn. ( bạn xem tiếp dưới )

## Vậy ta sẽ giải quyết ra sao

Dùng trình gỡ lỗi gdb

```c
   Dump of assembler code for function main:
   0x080484cd <+0>:     push   ebp
   0x080484ce <+1>:     mov    ebp,esp
   0x080484d0 <+3>:     push   edi
   0x080484d1 <+4>:     and    esp,0xfffffff0
   0x080484d4 <+7>:     sub    esp,0x90
   0x080484da <+13>:    mov    eax,DWORD PTR [ebp+0xc]
   0x080484dd <+16>:    mov    DWORD PTR [esp+0x1c],eax
   0x080484e1 <+20>:    mov    eax,gs:0x14
   0x080484e7 <+26>:    mov    DWORD PTR [esp+0x8c],eax
   0x080484ee <+33>:    xor    eax,eax
   0x080484f0 <+35>:    cmp    DWORD PTR [ebp+0x8],0x1
   0x080484f4 <+39>:    jg     0x8048514 <main+71>
   0x080484f6 <+41>:    mov    eax,DWORD PTR [esp+0x1c]
   0x080484fa <+45>:    mov    edx,DWORD PTR [eax]
   0x080484fc <+47>:    mov    eax,0x8048680
   0x08048501 <+52>:    mov    DWORD PTR [esp+0x4],edx
   0x08048505 <+56>:    mov    DWORD PTR [esp],eax
   0x08048508 <+59>:    call   0x8048380 <printf@plt>
   0x0804850d <+64>:    mov    eax,0x0
   0x08048512 <+69>:    jmp    0x8048592 <main+197>
   0x08048514 <+71>:    mov    eax,DWORD PTR [esp+0x1c]
   0x08048518 <+75>:    add    eax,0x4
   0x0804851b <+78>:    mov    eax,DWORD PTR [eax]
   0x0804851d <+80>:    mov    DWORD PTR [esp+0x18],0xffffffff
   0x08048525 <+88>:    mov    edx,eax
   0x08048527 <+90>:    mov    eax,0x0
   0x0804852c <+95>:    mov    ecx,DWORD PTR [esp+0x18]
   0x08048530 <+99>:    mov    edi,edx
   0x08048532 <+101>:   repnz scas al,BYTE PTR es:[edi]
   0x08048534 <+103>:   mov    eax,ecx
   0x08048536 <+105>:   not    eax
   0x08048538 <+107>:   sub    eax,0x1
   0x0804853b <+110>:   cmp    eax,0x14
   0x0804853e <+113>:   je     0x8048553 <main+134>
   0x08048540 <+115>:   mov    DWORD PTR [esp],0x8048698
   0x08048547 <+122>:   call   0x80483a0 <puts@plt>
   0x0804854c <+127>:   mov    eax,0x0
   0x08048551 <+132>:   jmp    0x8048592 <main+197>
   0x08048553 <+134>:   mov    eax,DWORD PTR [esp+0x1c]
   0x08048557 <+138>:   add    eax,0x4
   0x0804855a <+141>:   mov    eax,DWORD PTR [eax]
   0x0804855c <+143>:   mov    DWORD PTR [esp],eax
   0x0804855f <+146>:   call   0x8048494 <check_password>
   0x08048564 <+151>:   mov    edx,DWORD PTR ds:0x804a020
   0x0804856a <+157>:   cmp    eax,edx
   0x0804856c <+159>:   jne    0x8048581 <main+180>
   0x0804856e <+161>:   mov    DWORD PTR [esp],0x80486bb
   0x08048575 <+168>:   call   0x80483b0 <system@plt>
   0x0804857a <+173>:   mov    eax,0x0
   0x0804857f <+178>:   jmp    0x8048592 <main+197>
   0x08048581 <+180>:   mov    DWORD PTR [esp],0x80486c9
   0x08048588 <+187>:   call   0x80483a0 <puts@plt>
   0x0804858d <+192>:   mov    eax,0x0
   0x08048592 <+197>:   mov    edx,DWORD PTR [esp+0x8c]
   0x08048599 <+204>:   xor    edx,DWORD PTR gs:0x14
   0x080485a0 <+211>:   je     0x80485a7 <main+218>
   0x080485a2 <+213>:   call   0x8048390 <__stack_chk_fail@plt>
   0x080485a7 <+218>:   mov    edi,DWORD PTR [ebp-0x4]
   0x080485aa <+221>:   leave
   0x080485ab <+222>:   ret
End of assembler dump.
```

## Step 1

Sử dụng gdb

```c
[-------------------------------------code-------------------------------------]
   0x80484c6 <check_password+50>:       jle    0x80484b0 <check_password+28>
   0x80484c8 <check_password+52>:       mov    eax,DWORD PTR [ebp-0x8]
   0x80484cb <check_password+55>:       leave
=> 0x80484cc <check_password+56>:       ret
   0x80484cd <main>:    push   ebp
   0x80484ce <main+1>:  mov    ebp,esp
   0x80484d0 <main+3>:  push   edi
   0x80484d1 <main+4>:  and    esp,0xfffffff0
[------------------------------------stack-------------------------------------]
0000| 0xffa67b3c --> 0x8048564 (<main+151>:     mov    edx,DWORD PTR ds:0x804a020)
0004| 0xffa67b40 --> 0xffa67de2 ('A' <repeats 20 times>)
0008| 0xffa67b44 --> 0x1
0012| 0xffa67b48 --> 0xc2
0016| 0xffa67b4c --> 0xf75b379b (add    esp,0x10)
0020| 0xffa67b50 --> 0xffa67b7e --> 0xffff0000
0024| 0xffa67b54 --> 0xffa67c80 --> 0xffa67df7 ("XDG_SESSION_ID=38594")
0028| 0xffa67b58 --> 0xffffffff
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x080484cc in check_password ()
gdb-peda$ n
[----------------------------------registers-----------------------------------]
EAX: 0x46464645 ('EFFF')
EBX: 0x0
ECX: 0xffffffea
EDX: 0xffa67de2 ('A' <repeats 20 times>)
ESI: 0xf76d6000 --> 0x1b2db0
EDI: 0xffa67df7 ("XDG_SESSION_ID=38594")
EBP: 0xffa67bd8 --> 0x0
ESP: 0xffa67b40 --> 0xffa67de2 ('A' <repeats 20 times>)
EIP: 0x8048564 (<main+151>:     mov    edx,DWORD PTR ds:0x804a020)
EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x804855a <main+141>:        mov    eax,DWORD PTR [eax]
   0x804855c <main+143>:        mov    DWORD PTR [esp],eax
   0x804855f <main+146>:        call   0x8048494 <check_password>
=> 0x8048564 <main+151>:        mov    edx,DWORD PTR ds:0x804a020
   0x804856a <main+157>:        cmp    eax,edx
   0x804856c <main+159>:        jne    0x8048581 <main+180>
   0x804856e <main+161>:        mov    DWORD PTR [esp],0x80486bb
   0x8048575 <main+168>:        call   0x80483b0 <system@plt>
[------------------------------------stack-------------------------------------]
0000| 0xffa67b40 --> 0xffa67de2 ('A' <repeats 20 times>)
0004| 0xffa67b44 --> 0x1
0008| 0xffa67b48 --> 0xc2
0012| 0xffa67b4c --> 0xf75b379b (add    esp,0x10)
0016| 0xffa67b50 --> 0xffa67b7e --> 0xffff0000
0020| 0xffa67b54 --> 0xffa67c80 --> 0xffa67df7 ("XDG_SESSION_ID=38594")
0024| 0xffa67b58 --> 0xffffffff
0028| 0xffa67b5c --> 0xffa67c74 --> 0xffa67dd4 ("/home/col/col")
[------------------------------------------------------------------------------]
```

## Step 2

Ta set break tại giá trị ret hàm check.

```c
 0x80484c6 <check_password+50>:       jle    0x80484b0 <check_password+28>
   0x80484c8 <check_password+52>:       mov    eax,DWORD PTR [ebp-0x8]
   0x80484cb <check_password+55>:       leave
=> 0x80484cc <check_password+56>:       ret
   0x80484cd <main>:    push   ebp
   0x80484ce <main+1>:  mov    ebp,esp
   0x80484d0 <main+3>:  push   edi
   0x80484d1 <main+4>:  and    esp,0xfffffff0
[------------------------------------stack-------------------------------------]
0000| 0xffa67b3c --> 0x8048564 (<main+151>:     mov    edx,DWORD PTR ds:0x804a020)
0004| 0xffa67b40 --> 0xffa67de2 ('A' <repeats 20 times>)
0008| 0xffa67b44 --> 0x1
0012| 0xffa67b48 --> 0xc2
0016| 0xffa67b4c --> 0xf75b379b (add    esp,0x10)
0020| 0xffa67b50 --> 0xffa67b7e --> 0xffff0000
0024| 0xffa67b54 --> 0xffa67c80 --> 0xffa67df7 ("XDG_SESSION_ID=38594")
0028| 0xffa67b58 --> 0xffffffff

0x804855a <main+141>:        mov    eax,DWORD PTR [eax]
   0x804855c <main+143>:        mov    DWORD PTR [esp],eax
   0x804855f <main+146>:        call   0x8048494 <check_password>
=> 0x8048564 <main+151>:        mov    edx,DWORD PTR ds:0x804a020
   0x804856a <main+157>:        cmp    eax,edx
   0x804856c <main+159>:        jne    0x8048581 <main+180>
   0x804856e <main+161>:        mov    DWORD PTR [esp],0x80486bb
   0x8048575 <main+168>:        call   0x80483b0 <system@plt>
[------------------------------------stack-------------------------------------]
0000| 0xffa67b40 --> 0xffa67de2 ('A' <repeats 20 times>)
0004| 0xffa67b44 --> 0x1
0008| 0xffa67b48 --> 0xc2
0012| 0xffa67b4c --> 0xf75b379b (add    esp,0x10)
0016| 0xffa67b50 --> 0xffa67b7e --> 0xffff0000
0020| 0xffa67b54 --> 0xffa67c80 --> 0xffa67df7 ("XDG_SESSION_ID=38594")
0024| 0xffa67b58 --> 0xffffffff
0028| 0xffa67b5c --> 0xffa67c74 --> 0xffa67dd4 ("/home/col/col")
[------------------------------------------------------------------------------]
```

Kết quả trả lại trong thanh ghi eax, nếu không bằng thì false.

Vậy nếu ta thanh đổi giá trị eax = 568134124

```
Continuing.
[Detaching after fork from child process 3166]
/bin/cat: flag: No such file or directory
[Inferior 1 (process 3101) exited normally]
```

Có vẻ như thành công rồi mà , làm sao để tìm giá trị trả về tính toán là bao nhiêu

## Step 3

Cùng đi tìm hiểu sâu xem .

```c
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
            res += ip[i];
        }
        return res;
```

Như ta thấy đầu vào được chuyển sang nguyên cả , với cả sau đó tính tổng .

vậy ta thử lấy độ dài là 20 chia cho 4 thì ra được 5 , vậy thì ta sẽ nghĩ ngay là 5 phần

mỗi phần là 4 byte

Hãy tưởng tượng xem

````c
"AAAA" + "AAAA" + "AAAA" + "AAAA" + "AAAA"
0x41414141 + 0x41414141 + 0x41414141 + 0x41414141 + 0x41414141
1094795585 + 1094795585 + 1094795585 + 1094795585 + 1094795585
res = 5473977925
```c
Thử cho đầu vào khác xem.

root@kali:~/Desktop/pwnable.kr/collision/test# ./test "AAAABBBBCCCCDDDDEEEE"         
hashcode : 568134124

--------------------------
loop :  0
piece value : 1094795585


--------------------------
loop :  1
piece value : 1111638594


--------------------------
loop :  2
piece value : 1128481603


--------------------------
loop :  3
piece value : 1145324612


--------------------------
loop :  4
piece value : 1162167621

wrong passcode.
````

```c
kết quả 
>>> 0x41414141
1094795585
>>> 0x42424242
1111638594
>>> 0x43434343
1128481603
>>> 0x44444444
1145324612
>>> 0x45454545
1162167621
```

## Khai thác

* lấy 568134124 / 5 = 113626824
* 568134124 % 5 = 4
* 113626824 \* 4 = 454507296
* 568134124 - 454507296 = 113626828

Cuối cùng convert qua hex

```python
>>> hex(113626824)
'0x6c5cec8'
>>> hex(113626828)
'0x6c5cecc'
```

```python
from pwn import *

payload = '\xc8\xce\xc5\x06'*4 + '\xcc\xce\xc5\x06'
s = ssh(user='col', host='pwnable.kr', port=2222, password='guest')
p = s.process(executable='./col',argv=['fd',payload])

p.interactive()
```

```
flag : daddy! I just managed to create a hash collision :)
```

Qủa là một phân tích dài , lúc đầu chơi pwn mình cũng có chơi re nên biết ít kiến thức nhưng cũng chưa hiểu nhiều đây bài pwn cơ bản mình chơi
