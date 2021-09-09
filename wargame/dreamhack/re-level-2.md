---
description: 'https://dreamhack.io/wargame/challenges/16/'
---

# Re Level 2

## Solution

Check file :

```
$file chall2.exe
```

Load IDA Phân tích:

![IDA](../../.gitbook/assets/image%20%282%29.png)

{% code title="hello.sh" %}
```cpp
__int64 __fastcall sub_140001000(__int64 a1)
{
  int i; // [rsp+0h] [rbp-18h]

  for ( i = 0; (unsigned __int64)i < 0x12; ++i )
  {
    if ( *(_DWORD *)&aC[4 * i] != *(unsigned __int8 *)(a1 + i) )
      return 0i64;
  }
  return 1i64;
}
```
{% endcode %}

Hàm này là hàm so sánh pass trong ida \( mã giả \)

Dword là 32 bit được lưu trữ bằng thanh ghi RCX

```c
movsxd  rax, [rsp+18h+Input]          => mang ky tư input
lea     rcx, aC         ; "C"
movsxd  rdx, [rsp+18h+Input]
mov     r8, [rsp+18h+arg_0]
movzx   edx, byte ptr [r8+rdx]   
cmp     [rcx+rax*4], edx     => rcx + rax*4 lấy giá trị ' c' so voi Cac ky tu input
jz      short loc_140001046
```

```c
Tại vung nhơ ac đưa vào rcx có các chuỗi ký tự này
aC              db 'C',0                ; DATA XREF: sub_140001000+28↑o
.data:0000000140003002                 align 4
.data:0000000140003004 aO              db 'o',0
.data:0000000140003006                 align 8
.data:0000000140003008 aM              db 'm',0
.data:000000014000300A                 align 4
.data:000000014000300C aP              db 'p',0
.data:000000014000300E                 align 10h
.data:0000000140003010 a4              db '4',0
.data:0000000140003012                 align 4
.data:0000000140003014 aR              db 'r',0
.data:0000000140003016                 align 8
.data:0000000140003018 aE              db 'e',0
.data:000000014000301A                 align 4
.data:000000014000301C                 db '_',0
.data:000000014000301E                 align 20h
.data:0000000140003020 aT              db 't',0
.data:0000000140003022                 align 4
.data:0000000140003024                 db 'h',0
.data:0000000140003026                 align 8
.data:0000000140003028 aE_0            db 'e',0
.data:000000014000302A                 align 4
.data:000000014000302C                 db '_',0
.data:000000014000302E                 align 10h
.data:0000000140003030 aA              db 'a',0
.data:0000000140003032                 align 4
.data:0000000140003034 aR_0            db 'r',0
.data:0000000140003036                 align 8
.data:0000000140003038 aR_1            db 'r',0
.data:000000014000303A                 align 4
.data:000000014000303C a4_0            db '4',0
.data:000000014000303E                 align 20h
.data:0000000140003040 aY              db 'y',0
```

Ta ghép nó lại sẽ ra 

Flag : Comp4re\__the\_arr4y_

