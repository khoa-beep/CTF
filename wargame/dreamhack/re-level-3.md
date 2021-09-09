# Re Level 3

## Solution

Check file:

```
$ file chall3.exe
```

File này được tạo trên nền tảng window và code bằng c++

Phân tích IDA

![IDA](../../.gitbook/assets/image%20%281%29.png)

{% code title="file chall3" %}
```c
__int64 __fastcall sub_140001000(__int64 input)
{
  int i; // [rsp+0h] [rbp-18h]

  for ( i = 0; (unsigned __int64)i < 0x18; ++i )
  {
    if ( byte_140003000[i] != (i ^ *(unsigned __int8 *)(input + i)) + 2 * i )
      return 0i64;
  }
  return 1i64;
}
```
{% endcode %}

Hàm mã giả c ta thấy nó đem ký tự nhập đi xor với byte\_14003000 

Hint : ý tưởng ở đây mình sẽ đem byte\_140003000 và code lại theo công thức tính toán trên là ra flag

vào trong chỗ byte\_140003000 xem có những dữ liệu gì trong đó

```c
byte_140003000  db 73, 96, 103, 116, 99, 103, 66, 102, 128, 120, 2 dup(105)
.data:0000000140003000                                         ; DATA XREF: sub_140001000+28↑o
.data:0000000140003000                 db 123, 153, 109, 136, 104, 148, 159, 141, 77, 165, 157
.data:0000000140003000                 db 69, 8 dup(0)
```

```python
# sau khi xong ta đem theo côn thức như trong IDA phân tichcs ta code raddc gì
arr_byte = [73, 96, 103, 116, 99, 103, 66, 102, 128, 120, 105, 105, 123, 153, 109, 136, 104, 148, 159, 141, 77, 165, 157, 69]
flag = ''
for i in range(0,len(arr_byte)):
    flag += chr(arr_byte[i] - (2*i)^i)
print("DH{{{}}}".format(''.join(flag)))
```

Ta được flag : DH{I\_am\_X0\_xo\_Xor\_eXcit1ng}

Đem cái pass ta vừa tìm được và  thử đăng nhập vào xem

![](../../.gitbook/assets/image%20%284%29.png)

Kết quả là ta đã truy cập vào thành công

