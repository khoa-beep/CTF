# Thử thách Crackme 1 \( Very Easy\)

Qua bài giới thiệu mình viết trước kia về x64 DBG thì bài này mình viết về giải quyết một target rất đơn giản thôi . Let' go nào :v

File target :

{% file src="../../.gitbook/assets/easy-crackme1.rar" caption="easy-crackme1" %}

### 1.

Bước đầu tiên ta cần làm là mở chương trình lên và chạy thử

```text
khoa@DESKTOP:/mnt/c/Users/DELL/Downloads$ file easy-crackme1.exe
easy-crackme1.exe: PE32+ executable (console) x86-64, for MS Windows
```

Mã trên mình chạy trên Terminal trên hệ điều hành linux



Vào công việc chính thôi .

Ta có thẩy chương trình cho ta nhập vào 2  số 1 lần .

![](../../.gitbook/assets/image%20%285%29.png)

Thử load vào x64 DBG xem sao 

![](../../.gitbook/assets/image%20%283%29.png)

Làm như hình trên để tìm hàm nhập chuỗi 

```text
0000000140001200 | 48:83EC 38                    | sub rsp,38                              |
0000000140001204 | 48:8D0D 25100000              | lea rcx,qword ptr ds:[140002230]        | 0000000140002230:"input: "
000000014000120B | E8 60FEFFFF                   | call easy-crackme1.140001070            |
0000000140001210 | 4C:8D4424 20                  | lea r8,qword ptr ss:[rsp+20]            |
0000000140001215 | 48:8D5424 24                  | lea rdx,qword ptr ss:[rsp+24]           |
000000014000121A | 48:8D0D 17100000              | lea rcx,qword ptr ds:[140002238]        | 0000000140002238:"%d %d"
0000000140001221 | E8 FAFEFFFF                   | call easy-crackme1.140001120            | scanf
0000000140001226 | 8B5424 20                     | mov edx,dword ptr ss:[rsp+20]           |
000000014000122A | 8B4C24 24                     | mov ecx,dword ptr ss:[rsp+24]           |
000000014000122E | E8 4DFFFFFF                   | call easy-crackme1.140001180            | Check_pass
0000000140001233 | 85C0                          | test eax,eax                            |   
0000000140001235 | 74 0F                         | je easy-crackme1.140001246              |
0000000140001237 | 48:8D0D 02100000              | lea rcx,qword ptr ds:[140002240]        | 0000000140002240:"correct!"
000000014000123E | FF15 440F0000                 | call qword ptr ds:[<&puts>]             |
0000000140001244 | EB 0D                         | jmp easy-crackme1.140001253             |
0000000140001246 | 48:8D0D FF0F0000              | lea rcx,qword ptr ds:[14000224C]        | 000000014000224C:"wrong!"
000000014000124D | FF15 350F0000                 | call qword ptr ds:[<&puts>]             |
0000000140001253 | 33C0                          | xor eax,eax                             |
0000000140001255 | 48:83C4 38                    | add rsp,38                              |
0000000140001259 | C3                            | ret                                     |
```

Một vài dòng mã mình đã chú thích trên ta sẽ vào hàm 

```text
easy-crackme1.140001180
```

Đi vào bên trong phân tích

```text
0000000140001194 | 77 0A                         | ja easy-crackme1.1400011A0              |
0000000140001196 | 817C24 28 00200000            | cmp dword ptr ss:[rsp+28],2000          | input2
000000014000119E | 76 04                         | jbe easy-crackme1.1400011A4             |
00000001400011A0 | 33C0                          | xor eax,eax                             |
00000001400011A2 | EB 4F                         | jmp easy-crackme1.1400011F3             |
00000001400011A4 | 8B4424 20                     | mov eax,dword ptr ss:[rsp+20]           |
00000001400011A8 | 0FAF4424 28                   | imul eax,dword ptr ss:[rsp+28]          | input1= input1 * input2
00000001400011AD | 890424                        | mov dword ptr ss:[rsp],eax              | [rsp] = input1
00000001400011B0 | 33D2                          | xor edx,edx                             | edx = 0
00000001400011B2 | 8B4424 20                     | mov eax,dword ptr ss:[rsp+20]           | eax = input1
00000001400011B6 | F77424 28                     | div dword ptr ss:[rsp+28]               | eax = input1 / input2
00000001400011BA | 894424 04                     | mov dword ptr ss:[rsp+4],eax            |
00000001400011BE | 8B4424 28                     | mov eax,dword ptr ss:[rsp+28]           | input2
00000001400011C2 | 8B4C24 20                     | mov ecx,dword ptr ss:[rsp+20]           | input1
00000001400011C6 | 33C8                          | xor ecx,eax                             | ecx = input2 ^ input1
00000001400011C8 | 8BC1                          | mov eax,ecx                             | eax = ecx
00000001400011CA | 894424 08                     | mov dword ptr ss:[rsp+8],eax            | eax
00000001400011CE | 813C24 BCE96A00               | cmp dword ptr ss:[rsp],6AE9BC           |
00000001400011D5 | 75 1A                         | jne easy-crackme1.1400011F1             |
00000001400011D7 | 837C24 04 04                  | cmp dword ptr ss:[rsp+4],4              |
00000001400011DC | 75 13                         | jne easy-crackme1.1400011F1             |
00000001400011DE | 817C24 08 FC120000            | cmp dword ptr ss:[rsp+8],12FC           |
00000001400011E6 | 75 09                         | jne easy-crackme1.1400011F1             |
00000001400011E8 | B8 01000000                   | mov eax,1                               |
00000001400011ED | EB 04                         | jmp easy-crackme1.1400011F3             |
00000001400011EF | EB 02                         | jmp easy-crackme1.1400011F3             |
00000001400011F1 | 33C0                          | xor eax,eax                             |
00000001400011F3 | 48:83C4 18                    | add rsp,18                              |
00000001400011F7 | C3                            | ret                                     |
```

Ta phân tích được và có được công thức trên sẽ là :

CT :  ở đây mình đặt theo giá trị x1 , x2 ...

x1 = input1 \* input2  == 0x6ae9b 

x2 = input1 / input2  == 4

x3 =  input2 ^ input1 == 0x12fc



Ta sẽ viết code keygen lại ct theo công thức tính toán trên 

```python
for x in range(0,0x2000+1):
    for y in range(0,0x2000+1):
        if (x*y != 0x6ae9bc):
            continue
        if(x // y != 4):
            continue
        if(x ^ y != 0x12fc):
            continue
        print("x = ", x, "y = ",y)
# x = 5678 , y = 1234
```

![](../../.gitbook/assets/image%20%287%29.png)

Chính xác rồi :v có vẻ như rất easy game, kết thúc này mình có 1 bài tập dành cho các bạn hay giải nó và thử thách bản thân nghe :v

{% file src="../../.gitbook/assets/re3.zip" caption="easy-crackme-very-essyyyyyy" %}

