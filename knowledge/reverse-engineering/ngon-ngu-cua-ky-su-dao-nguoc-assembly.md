# Ngôn ngữ của kỹ sư đảo ngược: Assembly

Có một thế giới rộng lớn bên trong máy tính. Các mối quan hệ nhân quả logic phức tạp tồn tại, nhiều thực thể tương tác và có một ngôn ngữ gọi là Mã máy được sử dụng trong thế giới đó. Và những gì người kỹ sư đảo ngược làm là hiểu được hành vi của thế giới rộng lớn đó. Để làm được điều này, một trong những kỹ năng cơ bản mà một kỹ sư đảo ngược phải có là hiểu ngôn ngữ của máy tính.

Nhưng vấn đề là ngôn ngữ máy, ngôn ngữ của máy tính, rất khác với ngôn ngữ hàng ngày của chúng ta. Ngôn ngữ máy chỉ được tạo thành từ 0 và 1, vì vậy chúng ta rất khó hiểu câu dựa trên từ.



![](../../.gitbook/assets/image%20%289%29.png)

May mắn thay, ngôn ngữ máy là bí truyền, ngay cả đối với các nhà phát triển máy tính ban đầu đang viết mã bằng ngôn ngữ máy. Vì vậy, một trong những nhà khoa học máy tính, David Wheeler, đã phát minh ra Hợp ngữ và Trình lắp ráp trong khi phát triển EDSAC.

Trình hợp ngữ là một loại trình thông dịch, nơi các nhà phát triển viết mã bằng hợp ngữ và dịch mã sang ngôn ngữ máy mà máy tính có thể hiểu được. Vì ngôn ngữ hợp ngữ dễ hiểu hơn nhiều so với ngôn ngữ máy, các nhà phát triển có thể phát triển thuận tiện hơn.

Tuy nhiên, những người tháo gỡ phần mềm lại có ý kiến ​​ngược lại và phát triển một trình tháo gỡ có thể chuyển ngôn ngữ máy sang hợp ngữ. Khi phần mềm bao gồm ngôn ngữ máy được đưa vào một trình tháo gỡ, nó sẽ được dịch thành mã hợp ngữ. Điều này loại bỏ sự cần thiết của các nhà phân tích phần mềm đọc ngôn ngữ máy để phân tích phần mềm.

Các kiến ​​trúc phổ biến, bao gồm x86-64 được đề cập trong chương trình giảng dạy, rất dễ tìm thấy trên Internet. Vì vậy, nếu bạn chỉ có thể hiểu hợp ngữ, bạn có thể phân tích phần mềm bằng cách sử dụng trình tháo gỡ.

Trong hai khóa học tiếp theo của giáo trình này, chúng tôi sẽ giới thiệu tổng quan về hợp ngữ và giới thiệu các hướng dẫn cho x86-64. Sau khi lấy nó, bạn sẽ có kiến ​​thức ngôn ngữ cơ bản để đọc phần mềm.





1. **Hợp ngữ và x86-64**

Hợp ngữ

Như đã đề cập trước đó, hợp ngữ là một ngôn ngữ được thay thế cho ngôn ngữ máy của máy tính. Điều này có nghĩa là nếu có nhiều loại ngôn ngữ máy thì cũng phải có nhiều loại hợp ngữ. Và, như tôi đã nói khi giải thích Kiến trúc tập lệnh \(ISA\), có nhiều loại ISA khác nhau được sử dụng trong CPU, chẳng hạn như IA-32, x86-64, ARM và MIPS.

Vì vậy, có bao nhiêu hợp ngữ như có chúng. Thế giới x64 có ngôn ngữ hợp ngữ là x64 và thế giới ARM có ngôn ngữ hợp ngữ là ARM. Bạn càng biết nhiều ngôn ngữ này, thì càng tốt. Tuy nhiên, vì chương trình học này nhắm mục tiêu đến kiến ​​trúc x64, chúng tôi sẽ chỉ giới thiệu hợp ngữ x64. Các ngôn ngữ khác sẽ có cơ hội được đề cập chi tiết trong các chương trình giảng dạy khác.

## Cấu trúc cơ bản

Khi bạn đọc một câu, bạn hiểu chủ ngữ là gì, tân ngữ là gì, từ đó đưa ra ý nghĩa ngữ pháp của từ và hiểu được câu. Và đối với hợp ngữ cũng vậy.

Hợp ngữ x64 có cú pháp đơn giản hơn nhiều so với tiếng Hàn mà chúng ta sử dụng. Các câu của chúng bao gồm một lệnh \(Mã hoạt động, Opcode\) tương ứng với một động từ và một toán hạng \(Operand\) tương ứng với một đối tượng.



![](../../.gitbook/assets/image%20%2810%29.png)

### Lệnh 🔫

Intel x64 có rất nhiều hướng dẫn. Trong chương trình học này, bạn sẽ nghiên cứu chi tiết 21 lệnh quan trọng trong khóa học này và khóa học tiếp theo.

Các lệnh được học có thể được phân loại như sau.

Truyền dữ liệu

mov, Lea

Môn số học

inc, dec, add, sub

Hoạt động logic

thêm, hoặc, xor, không

So sánh

cmp, kiểm tra

Chi nhánh

jmp, je, jg

Cây rơm

đẩy pop

Thủ tục

gọi, bắt lại, rời đi

Cuộc gọi hệ thống

syscall

### Toán hạng🎯

Có ba loại toán hạng.

```text
 Giá trị tức thì (Value)

 Đăng ký  ( Register )

 Kỉ niệm  ( Menmory )
```

Toán hạng bộ nhớ được thể hiện như trong \[\] và một PTR chỉ thị kích thước TYPE có thể được thêm vào trước. Ở đây, BYTE, WORD, DWORD và QWORD có thể được sử dụng làm kiểu và kích thước của 1 byte, 2 byte, 4 byte và 8 byte được chỉ định tương ứng.



## 👇 Ví dụ về toán hạng bộ nhớ

QWORD PTR \[0x8048000\]

Tham chiếu 8 byte dữ liệu ở 0x8048000

DWORD PTR \[0x8048000\]

Tham khảo dữ liệu ở 0x8048000 x 4 byte

WORD PTR \[rax\]

Dữ liệu được tham chiếu bởi 2 byte tại địa chỉ được trỏ tới bởi rax.



#### Note

🦜 Tại sao kích thước của kiểu dữ liệu WORD là 2 byte

Ban đầu, Intel phát triển kiến ​​trúc IA-16, trong đó các WORD có kích thước 16 bit. Vì WORD của CPU là 16 bit, điều tự nhiên là định nghĩa WORD là kiểu dữ liệu 16 bit ngay cả trong hợp ngữ.

Các kiến ​​trúc IA-32 và x86-64 được phát triển sau này có CPU WORD được mở rộng lên 32-bit và 64-bit. Do đó, trong hai kiến ​​trúc này, việc chỉ định kích thước của kiểu dữ liệu WORD 32-bit và 64-bit dường như là tự nhiên.

Tuy nhiên, Intel vẫn giữ kích thước của kiểu dữ liệu WORD là 16 bit. Điều này là do, nếu bạn thay đổi kích thước của kiểu dữ liệu WORD, các chương trình hiện có có thể không tương thích với kiến ​​trúc mới. Vì vậy, Intel đã giữ nguyên kích thước của WORD hiện có và thêm các kiểu dữ liệu DWORD \(Double Word, 32bit\) và QWORD \(Quad Word, 64bit\).

#### Hướng lắp ráp x86-64

Di chuyển dữ liệu🚚

Một lệnh di chuyển dữ liệu chỉ dẫn một giá trị được di chuyển vào một thanh ghi hoặc bộ nhớ.

mov dst, src: Gán giá trị trong src thành dst

mov rdi, rsi

Thay giá trị của rsi thành rdi

mov QWORD PTR \[rdi\], rsi

Gán giá trị của rsi cho địa chỉ được trỏ đến bởi rdi

mov QWORD PTR \[rdi + 8 \* rcx\], rsi

Gán giá trị của rsi cho địa chỉ được trỏ tới bởi rdi + 8 \* rcx

lea dst, src: Địa chỉ hiệu dụng \(EA\) của src được lưu trữ trong dst.

lea rsi, \[rbx + 8 \* rcx\]

Thay thế rbx + 8 \* rcx thành rsi



#### Bài tập



```text
[Memory]
0x401a40 | 0x0000000012345678
0x401a48 | 0x0000000000C0FFEE
0x401a50 | 0x00000000DEADBEEF
0x401a58 | 0x00000000CAFEBABE
0x401a60 | 0x0000000087654321
 =================================
 [Code]
 1: mov rax, [rbx+8]
 2: lea rax, [rbx+8]
```

Đọc và trả lời 

Khi thực thi tối đa 1, giá trị được lưu trữ trong rax là  gì ? 

Khi được thực thi tối đa, giá trị tính bằng rax là gì ? 



Phép toán số học❌

add dst, src: Thêm giá trị của src vào dst.



| add eax, 3 | eax += 3 |
| :--- | :--- |
| add ax, WORD PTR\[rdi\] | ax += \*\(WORD \*\)rdi |
| sub eax,3 | eax = eax - 3 |
| sub ax, WORD PTR\[rdi\] | ax -= _\(WORD_ \)rdi |
| inc eax | eax += 1 |
| dec eax | eax -= 1 |



```text
[Register]
rax = 0x31337
rbx = 0x555555554000
rcx = 0x2
=================================
[Memory]
0x555555554000| 0x0000000000000000
0x555555554008| 0x0000000000000001
0x555555554010| 0x0000000000000003
0x555555554018| 0x0000000000000005
0x555555554020| 0x000000000003133A
==================================[Code]
1: add rax, [rbx+rcx*8]
2: add rcx, 2
3: sub rax, [rbx+rcx*8]
4: inc rax
```

Code 1 :  Gía trị Rax sẽ tính như sau



```cpp
add rax, [rbx+rcx*8] 
// rax = 0x31337 + [0x555555554000+0x2+8]  // thay dau * thanh cong
// rax = 0x31337 + [0x555555554002+8]   // 0x5555555540010 
// ta có giá trị tính toán tại địa chỉ bộ nhớ là bằng 0x5555555540010 cho nên giá trị tại vùng nhớ đó là
// 0x0000000000000003
// ta lấy 0x0000000000000003 + 0x31337 = 0x3133a
// như vậy rax = 0x3133a
```

Code 3 : Gía trị Rax tính như sau

```cpp
sub rax, [rbx+rcx*8]
// rax = 0x3133a+ [0x555555554010+0x2+8]  // thay dau * thanh cong
// rax = 0x3133a+ [0x555555554012+8]   // 0x5555555540020 
// ta có giá trị tính toán tại địa chỉ bộ nhớ là bằng 0x5555555540020 cho nên giá trị tại vùng nhớ đó là
//  0x000000000003133A
// ta lấy  0x3133a - 0x000000000003133A= 0
// như vậy rax = 0
```

Code 4 : Gía trị Rax như sau

Bạn hãy test thử xem ra giá trị bao nhiêu hãy nhắn qua maill mình nha 

Email : khosasuke@gmail.com.

Còn Một vài toán hạng khác bạn có thể tham khảo thêm 2 loại toán hạng nữa là AND và OR tại Link này.

{% embed url="https://www.tutorialspoint.com/assembly\_programming/assembly\_logical\_instructions.htm" %}

#### Lệnh So sánh trong hợp ngữ



Lệnh cmp là lệnh so sánh nó như việc so sánh hai toán hạng với nhau.

Ta sẽ hiểu rõ lệnh này thông qua vài ví dụ.

Ta có ct so sánh đơn giản như này được viết bằng c

```cpp
#include <stdio.h>
 
/* function declaration */
int max(int num1, int num2);
 
int main () {

   /* local variable definition */
   int a = 100;
   int b = 200;
   int ret;
 
   /* calling a function to get max value */
   ret = max(a, b);
 
   printf( "Max value is : %d\n", ret );
 
   return 0;
}
 
/* function returning the max between two numbers */
int max(int num1, int num2) {

   /* local variable declaration */
   int result;
 
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}
```

Sau khi biên dịch sang mã hợp ngữ

```cpp
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     DWORD PTR [rbp-4], 100
        mov     DWORD PTR [rbp-8], 200
        mov     edx, DWORD PTR [rbp-8]
        mov     eax, DWORD PTR [rbp-4]
        mov     esi, edx
        mov     edi, eax
        call    max(int, int)
        mov     DWORD PTR [rbp-12], eax
        mov     eax, DWORD PTR [rbp-12]
        mov     esi, eax
        mov     edi, OFFSET FLAT:.LC0
        mov     eax, 0
        call    printf
        mov     eax, 0
        leave
        ret
max(int, int):
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-20], edi
        mov     DWORD PTR [rbp-24], esi
        mov     eax, DWORD PTR [rbp-20]
        cmp     eax, DWORD PTR [rbp-24]
        jle     .L4
        mov     eax, DWORD PTR [rbp-20]
        mov     DWORD PTR [rbp-4], eax
        jmp     .L5
.L4:
        mov     eax, DWORD PTR [rbp-24]
        mov     DWORD PTR [rbp-4], eax
.L5:
        mov     eax, DWORD PTR [rbp-4]
        pop     rbp
        ret
```

Sau khi biên dịch ta thấy được đây là mã lắp ráp.

Mình sẽ giải thích cho các bạn từng dòng lệnh.

Dòng lệnh này thiết lập stack frame

```cpp
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
```

Phân tích hàm main.



```cpp
        mov     DWORD PTR [rbp-4], 100
        mov     DWORD PTR [rbp-8], 200
        mov     edx, DWORD PTR [rbp-8]
        mov     eax, DWORD PTR [rbp-4]
        mov     esi, edx
        mov     edi, eax
```

Lệnh di chuyển dữ liệu mov

mov DWORD PRT \[rbp-4\],100 

lệnh này di chuyên 100 vào vùng nhớ stack

lệnh tiếp cũng tương tự

ta đến lệnh mov edx, DWORD PTR \[rbp-8\] nó sẽ di chuyển dữ liệu tại vùng nhớ đó vào edx \( lệnh tiếp theo tương tự \)



```cpp
call    max(int, int)
```

Lệnh call max gọi hàm tìm max.

Vào phân tích tìm max.



```cpp
max(int, int):
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-20], edi     => bien a = 100
        mov     DWORD PTR [rbp-24], esi     => bien b = 200
        mov     eax, DWORD PTR [rbp-20]     => eax = bien a
        cmp     eax, DWORD PTR [rbp-24]     => so sanh bien a voi bien b
        jle     .L4                         => jle ( neu a nho hon b ) nhay den l4
        mov     eax, DWORD PTR [rbp-20]     => ( cho nay lon hon thi thuc hien )  eax = a 
        mov     DWORD PTR [rbp-4], eax      => result = a
        jmp     .L5
.L4:
        mov     eax, DWORD PTR [rbp-24]     => eax = b 
        mov     DWORD PTR [rbp-4], eax      => tai vung nho nay no gan lai ket qua thi chac bien result = b
.L5:
        mov     eax, DWORD PTR [rbp-4]      => eax = result
        pop     rbp                         => ket thuc qua trinh thuc thi
        ret                                 => ket qua tra lai eax la bien result
```

Hàm này thi chăc printf rồi nên không cần bận tâm lắm.

```cpp
        mov     DWORD PTR [rbp-12], eax
        mov     eax, DWORD PTR [rbp-12]
        mov     esi, eax
        mov     edi, OFFSET FLAT:.LC0
        mov     eax, 0
        call    printf
```

Qua đây thì mình đã cho các bạn hiểu được mã hợp ngữ và mã c nó hoạt động ra sao

#### 



