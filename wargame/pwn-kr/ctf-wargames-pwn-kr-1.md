# CTF wargames Pwn Kr 1

* **Category:** PWN
* **Points:** 1

## Challenge

FD

## Solution

Mommy! what is a file descriptor in Linux? Source CODE

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
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
int fd = atoi( argv[1] ) - 0x1234;
int len = 0;
len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;
```

Một biểu thức tính toán nhưng phía bên phải lại sử dụng atoi để tính toán số lượng tham số , và biểu thức tính len = 0 , hàm atoi sử dụng chuyển 1 kiểu chuỗi về số thâp phân.

Vậy là số lượng đầu vào của ta chuyển sang number và - 0x1234.

Hàm read dùng để đọc file , hàm strcmp dùng để so sánh 2 chuỗi.

Nói chung làm sao để nó vằng ra cái /bin/cat flag là win game :))

## Vậy ta sẽ giải quyết ra sao

Dùng trình gỡ lỗi gdb

```c
   0x08048494 <+0>:     push   ebp
   0x08048495 <+1>:     mov    ebp,esp
   0x08048497 <+3>:     push   edi
   0x08048498 <+4>:     push   esi
   0x08048499 <+5>:     and    esp,0xfffffff0
   0x0804849c <+8>:     sub    esp,0x20
   0x0804849f <+11>:    cmp    DWORD PTR [ebp+0x8],0x1
   0x080484a3 <+15>:    jg     0x80484bb <main+39>
   0x080484a5 <+17>:    mov    DWORD PTR [esp],0x8048630
   0x080484ac <+24>:    call   0x8048380 <puts@plt>
   0x080484b1 <+29>:    mov    eax,0x0
   0x080484b6 <+34>:    jmp    0x8048559 <main+197>
   0x080484bb <+39>:    mov    eax,DWORD PTR [ebp+0xc]
   0x080484be <+42>:    add    eax,0x4
   0x080484c1 <+45>:    mov    eax,DWORD PTR [eax]
   0x080484c3 <+47>:    mov    DWORD PTR [esp],eax
   0x080484c6 <+50>:    call   0x80483d0 <atoi@plt>
   0x080484cb <+55>:    sub    eax,0x1234
   0x080484d0 <+60>:    mov    DWORD PTR [esp+0x18],eax
   0x080484d4 <+64>:    mov    DWORD PTR [esp+0x1c],0x0
   0x080484dc <+72>:    mov    DWORD PTR [esp+0x8],0x20
   0x080484e4 <+80>:    mov    DWORD PTR [esp+0x4],0x804a060
   0x080484ec <+88>:    mov    eax,DWORD PTR [esp+0x18]
   0x080484f0 <+92>:    mov    DWORD PTR [esp],eax
   0x080484f3 <+95>:    call   0x8048370 <read@plt>
   0x080484f8 <+100>:   mov    DWORD PTR [esp+0x1c],eax
   0x080484fc <+104>:   mov    edx,0x8048646
   0x08048501 <+109>:   mov    eax,0x804a060
   0x08048506 <+114>:   mov    ecx,0xa
   0x0804850b <+119>:   mov    esi,edx
   0x0804850d <+121>:   mov    edi,eax
   0x0804850f <+123>:   repz cmps BYTE PTR ds:[esi],BYTE PTR es:[edi]
   0x08048511 <+125>:   seta   dl
   0x08048514 <+128>:   setb   al
   0x08048517 <+131>:   mov    ecx,edx
   0x08048519 <+133>:   sub    cl,al
   0x0804851b <+135>:   mov    eax,ecx
   0x0804851d <+137>:   movsx  eax,al
   0x08048520 <+140>:   test   eax,eax
   0x08048522 <+142>:   jne    0x8048548 <main+180>
   0x08048524 <+144>:   mov    DWORD PTR [esp],0x8048650
   0x0804852b <+151>:   call   0x8048380 <puts@plt>
   0x08048530 <+156>:   mov    DWORD PTR [esp],0x804865c
   0x08048537 <+163>:   call   0x8048390 <system@plt>
   0x0804853c <+168>:   mov    DWORD PTR [esp],0x0
   0x08048543 <+175>:   call   0x80483b0 <exit@plt>
   0x08048548 <+180>:   mov    DWORD PTR [esp],0x804866a
   0x0804854f <+187>:   call   0x8048380 <puts@plt>
   0x08048554 <+192>:   mov    eax,0x0
   0x08048559 <+197>:   lea    esp,[ebp-0x8]
   0x0804855c <+200>:   pop    esi
   0x0804855d <+201>:   pop    edi
   0x0804855e <+202>:   pop    ebp
   0x0804855f <+203>:   ret
```

Ta thử đổi cái số 0x1234 to hex = 4660

và thử chạy xem ra kết quả gì. ồ nó dừng lại cho ta nhập gì đó

Nhập chuỗi LETMEWIN xem sao, thành công rồi

```
The flag : mommy! I think I know what a file descriptor is!!
```
