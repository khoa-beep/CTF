# Esay Rev

Run File  and Test Input

```text
$ ./baby_re_2
Looking for the flag?
Enter the key: test
Wrong! Try Again ...

```

![](../../.gitbook/assets/image%20%2832%29.png)

Sử Dụng Ghidra phân tích code .

Ta thấy chỗ local 14 == local 20  \( là input nhap vao \)

Có nghĩa là mk tại local 14 là ở dạng hex 0x140685 đổi ra thâp phân là 1312389

Và ta lấy flag 

$ ./baby\_re\_2 Looking for the flag? Enter the key: 1312389 GrabCON{y0u\_g0t\_it\_8bb31}

