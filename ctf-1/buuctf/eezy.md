# Eezy

Tải file và phẩn tích.

```text
khoa@DESKTOP-L14K8T1:/mnt/c/Users/DELL/Downloads/eezy$ file challenge
challenge: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=fe1f928c91a15ef046ef18e6eb2b34d88e29cc8e, for GNU/Linux 3.2.0, not stripped
```

Đây là file :  ELF 64 bit binary and dynamically linked.

Sử dụng câu lệnh tìm kiếm chuỗi trong file.

```text
khoa@DESKTOP-L14K8T1:/mnt/c/Users/DELL/Downloads/eezy$ strings challenge
```

```text
TamilCTF{D0n'T_tRy_ThI5_N3xT_tIm3}
        -------------------------------------------------------------
        |                   Welcome To TamilCTF                     |
        |------------------------------------------------------------
        |  Category : Rev Eng                                       |
        |                                       Name : Eezy         |
        |___________________________________________________________|
                [+]   Wrong Flag!!!!   [+]
                [+]   Correct Flag :)   [+]
TamilCTF{R3V3RS3_15_fUn}
```

Tại đây có 2 chuỗi đem 2 chuỗi nhập vào xem có phải hay không.

```text
  -------------------------------------------------------------
        |                   Welcome To TamilCTF                     |
        |------------------------------------------------------------
        |  Category : Rev Eng                                       |
        |                                       Name : Eezy         |
        |___________________________________________________________|

Enter the flag : TamilCTF{R3V3RS3_15_fUn}
Nope :(
```

```text
./challenge

        -------------------------------------------------------------
        |                   Welcome To TamilCTF                     |
        |------------------------------------------------------------
        |  Category : Rev Eng                                       |
        |                                       Name : Eezy         |
        |___________________________________________________________|

Enter the flag : TamilCTF{D0n'T_tRy_ThI5_N3xT_tIm3}
                [+]   Wrong Flag!!!!   [+]
```

2 chuỗi đều không có gì đúng, chắc phải load vào IDA or ghidra.

Phân tích Ghidra xem có gì trong.

```text
undefined8 main(void)

{
  char flag [48];
  
  FUNC12341();
  welcome();
  printf("Enter the flag : ");
  fgets(flag,0x1f,stdin);
  Check_len(flag);
  new_arr(flag);
  return 0;
}
```

Ham main ta có 2 hàm đó là check độ dài flag và hàm tao mang mới.

#### Hàm check

```text
void Check_len(char *param_1)

{
  size_t sVar1;
  
  sVar1 = strlen(param_1);
  if ((int)sVar1 != 30) {
    puts("Nope :( ");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  return;
}
```

Kiểm tra độ dài flag là 30 ký tự nếu không sẽ thoát.

```text
void new_arr(char *flag)

{
  size_t Len;
  char Copy_arr [36];
  int local_14;
  int local_10;
  int index;
  
  Len = strlen(flag);
  local_14 = (int)Len;
  local_10 = local_14;
  for (index = 0; local_10 = local_10 + -1, index < local_14; index = index + 1) {
    Copy_arr[index] = flag[local_10];
  }
  FUCN1236(Copy_arr);
  return;
}
```

Hàm này copy chuỗi, để ý có một hàm nữa 

```text
FUCN1236(Copy_arr)
```

Hàm này không biết nó làm gì vào xem thử

```text
void FUCN1236(long param_1)

{
  undefined local_48 [48];
  int local_18;
  int local_14;
  int local_10;
  int local_c;
  
  local_c = 0;
  local_18 = 30;
  for (local_10 = 0; local_10 < local_18; local_10 = local_10 + 2) {
    local_48[local_c] = *(undefined *)(param_1 + local_10);
    local_c = local_c + 1;
  }
  for (local_14 = 1; local_14 < local_18; local_14 = local_14 + 2) {
    local_48[local_c] = *(undefined *)(param_1 + local_14);
    local_c = local_c + 1;
  }
  FUNC12347(local_48);
  return;
}
```

Hình như copy lại nữa chắc không cần quan tâm đâu.Có 1 hàm nữa dưới vào xem thử có gì hot không.

```text

void FUNC12347(long param_1)

{
  long lVar1;
  undefined8 *puVar2;
  int aiStack312 [36];
  undefined8 local_a8;
  undefined4 local_a0;
  undefined4 local_9c;
  undefined4 local_98;
  undefined4 local_94;
  undefined4 local_90;
  undefined4 local_8c;
  undefined4 local_88;
  undefined4 local_84;
  undefined4 local_80;
  undefined4 local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60;
  undefined4 local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  int local_14;
  int local_10;
  int i;
  
  puVar2 = &local_a8;
  for (lVar1 = 0x11; lVar1 != 0; lVar1 = lVar1 + -1) {
    *puVar2 = 0;
    puVar2 = puVar2 + 1;
  }
  *(undefined4 *)puVar2 = 0;
  local_a8._0_4_ = 0x48;
  local_a8._4_4_ = 0x73;
  local_a0 = 0x76;
  local_9c = 4;
  local_98 = 0x74;
  local_94 = 0x6a;
  local_90 = 0x61;
  local_8c = 6;
  local_88 = 5;
  local_84 = 0x59;
  local_80 = 0x62;
  local_7c = 0x73;
  local_78 = 0x76;
  local_74 = 0x5c;
  local_70 = 0x54;
  local_6c = 0x14;
  local_68 = 0x41;
  local_64 = 0x59;
  local_60 = 0x58;
  local_5c = 0x41;
  local_58 = 5;
  local_54 = 0x6a;
  local_50 = 0x58;
  local_4c = 0x76;
  local_48 = 6;
  local_44 = 0x4e;
  local_40 = 0x61;
  local_3c = 0x59;
  local_38 = 0x58;
  local_34 = 0x61;
  local_14 = 0x1e;
  for (i = 0; i < local_14; i = i + 1) {
    aiStack312[i] = (int)(char)(*(byte *)(param_1 + i) ^ 0x35);
  }
  local_10 = 0;
  while( true ) {
    if (local_14 <= local_10) {
      puts("\t\t[+]   Correct Flag :)   [+]");
      return;
    }
    if (aiStack312[local_10] != *(int *)((long)&local_a8 + (long)local_10 * 4)) break;
    local_10 = local_10 + 1;
  }
  puts("\t\t[+]   Wrong Flag!!!!   [+]");
                    /* WARNING: Subroutine does not return */
  exit(1);
}


```

Như một thanh niên phá đảo thế giới ảo :\(\(\( , như nó đem các byte đi xor vơi 0x35

```text
        00101235 89  02           MOV        dword ptr [RDX ]=>local_a8 ,EAX
        00101237 48  83  c2  04    ADD        RDX ,0x4
        0010123b c7  85  60       MOV        dword ptr [RBP  + local_a8 ],0x48
                 ff  ff  ff 
                 48  00  00  00
        00101245 c7  85  64       MOV        dword ptr [RBP  + local_a4 ],0x73
                 ff  ff  ff 
                 73  00  00  00
        0010124f c7  85  68       MOV        dword ptr [RBP  + local_a0 ],0x76
                 ff  ff  ff 
                 76  00  00  00
        00101259 c7  85  6c       MOV        dword ptr [RBP  + local_9c ],0x4
                 ff  ff  ff 
                 04  00  00  00
        00101263 c7  85  70       MOV        dword ptr [RBP  + local_98 ],0x74
                 ff  ff  ff 
                 74  00  00  00
        0010126d c7  85  74       MOV        dword ptr [RBP  + local_94 ],0x6a
                 ff  ff  ff 
                 6a  00  00  00
        00101277 c7  85  78       MOV        dword ptr [RBP  + local_90 ],0x61
                 ff  ff  ff 
                 61  00  00  00
        00101281 c7  85  7c       MOV        dword ptr [RBP  + local_8c ],0x6
                 ff  ff  ff 
                 06  00  00  00
        0010128b c7  45  80       MOV        dword ptr [RBP  + local_88 ],0x5
                 05  00  00  00
        00101292 c7  45  84       MOV        dword ptr [RBP  + local_84 ],0x59
                 59  00  00  00
        00101299 c7  45  88       MOV        dword ptr [RBP  + local_80 ],0x62
                 62  00  00  00
        001012a0 c7  45  8c       MOV        dword ptr [RBP  + local_7c ],0x73
                 73  00  00  00
        001012a7 c7  45  90       MOV        dword ptr [RBP  + local_78 ],0x76
                 76  00  00  00
        001012ae c7  45  94       MOV        dword ptr [RBP  + local_74 ],0x5c
                 5c  00  00  00
        001012b5 c7  45  98       MOV        dword ptr [RBP  + local_70 ],0x54
                 54  00  00  00
        001012bc c7  45  9c       MOV        dword ptr [RBP  + local_6c ],0x14
                 14  00  00  00
        001012c3 c7  45  a0       MOV        dword ptr [RBP  + local_68 ],0x41
                 41  00  00  00
        001012ca c7  45  a4       MOV        dword ptr [RBP  + local_64 ],0x59
                 59  00  00  00
        001012d1 c7  45  a8       MOV        dword ptr [RBP  + local_60 ],0x58
                 58  00  00  00
        001012d8 c7  45  ac       MOV        dword ptr [RBP  + local_5c ],0x41
                 41  00  00  00
        001012df c7  45  b0       MOV        dword ptr [RBP  + local_58 ],0x5
                 05  00  00  00
        001012e6 c7  45  b4       MOV        dword ptr [RBP  + local_54 ],0x6a
                 6a  00  00  00
        001012ed c7  45  b8       MOV        dword ptr [RBP  + local_50 ],0x58
                 58  00  00  00
        001012f4 c7  45  bc       MOV        dword ptr [RBP  + local_4c ],0x76
                 76  00  00  00
        001012fb c7  45  c0       MOV        dword ptr [RBP  + local_48 ],0x6
                 06  00  00  00
        00101302 c7  45  c4       MOV        dword ptr [RBP  + local_44 ],0x4e
                 4e  00  00  00
        00101309 c7  45  c8       MOV        dword ptr [RBP  + local_40 ],0x61
                 61  00  00  00
        00101310 c7  45  cc       MOV        dword ptr [RBP  + local_3c ],0x59
                 59  00  00  00
        00101317 c7  45  d0       MOV        dword ptr [RBP  + local_38 ],0x58
                 58  00  00  00
        0010131e c7  45  d4       MOV        dword ptr [RBP  + local_34 ],0x61
                 61  00  00  00
        00101325 c7  45  f4       MOV        dword ptr [RBP  + local_14 ],0x1e
                 1e  00  00  00
        0010132c c7  45  fc       MOV        dword ptr [RBP  + i],0x0
                 00  00  00  00
        00101333 eb  29           JMP        LAB_0010135e
                             LAB_00101335                                    XREF[1]:     00101364 (j)   
        00101335 8b  45  fc       MOV        EAX ,dword ptr [RBP  + i]
        00101338 48  63  d0       MOVSXD     RDX ,EAX
        0010133b 48  8b  85       MOV        RAX ,qword ptr [RBP  + local_140 ]
                 c8  fe  ff  ff
        00101342 48  01  d0       ADD        RAX ,RDX
        00101345 0f  b6  00       MOVZX      EAX ,byte ptr [RAX ]
        00101348 83  f0  35       XOR        EAX ,0x35


```



Hint: 

đem các byte đi xor 0x35

xong lưu vào 1 mảng 

Rồi đảo ngược lại dùng mảng mới.

```python
value = [0x48, 0x73, 0x76, 0x4, 0x74, 0x6a, 0x61, 0x6, 0x5, 0x59, 0x62, 0x73, 0x76, 0x5c, 0x54,
         0x14, 0x41, 0x59, 0x58, 0x41, 0x5, 0x6a, 0x58, 0x76, 0x6, 0x4e, 0x61, 0x59, 0x58, 0x61]
xor = 0x35
xor_s = []
for i in value:
    xor_s.append(chr(i ^ xor))
length = len(value)
i = 0
shuffle = ''
while i < length/2:
    shuffle += xor_s[i]
    shuffle += xor_s[i+15]
    i += 1
print(shuffle[::-1])

```

Flag : TamilCTF{W3lC0m3\_T0\_tAm1lCtF!}

