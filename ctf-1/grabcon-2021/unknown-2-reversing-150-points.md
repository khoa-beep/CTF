# Unknown 2 - Reversing - 150 points

Check information file 



```text
$ file med_re_2 
med_re_2: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), statically
linked, no section header
$ strings med_re_2 | grep UPX
...
$Info: This file is packed with the UPX executable packer http://upx.sf.net $

```

Ta thấy lệnh linux strings med\_re2 \| grep UPX là tìm kiếm thông tin dựa trên chuôi UPX

Thì thấy được file này bị pack lại nhắm che dấu thông tin nhằm tránh khỏi đảo ngược.



```text
$ ls -la med_re_2 
-rwxrw-rw- 1 root root 19952 Sep  5 15:49 med_re_2     

$ upx -d med_re_2                                                                                                                         
                       Ultimate Packer for eXecutables                                                       
                          Copyright (C) 1996 - 2020                                                           
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020                                 

        File size         Ratio      Format      Name                                                         
   --------------------   ------   -----------   -----------                                                 
     53088 <-     19952   37.58%   linux/amd64   med_re_2                                                    
     
Unpacked 1 file.                                                                                             
$ ls -la med_re_2                                                                                           
-rwxrw-rw- 1 root root 53088 Sep  5 15:49 med_re_2
$ file med_re_2
med_re_2: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically 
linked, interpreter /lib64/ld-linux-x86-64.so.2, 
BuildID[sha1]=8c647d87ce01879a967ee42dc5d9d4111a6b1b19, for GNU/Linux 3.2.0, 
with debug_info, not stripped
```

File sau khi khi được giải nén.

Run Program



```text
$ ./med_re_2

___.          .__                              
\_ |__ _____  |  | _____    ____   ____  ____  
 | __ \\__  \ |  | \__  \  /    \_/ ___\/ __ \ 
 | \_\ \/ __ \|  |__/ __ \|   |  \  \__\  ___/ 
 |___  (____  /____(____  /___|  /\___  >___  >
     \/     \/          \/     \/     \/    \/ 


Comparison is the death of joy.
```

![](../../.gitbook/assets/image%20%2833%29.png)

Phân tích dựa trên Ghidra

Trong ghidra, chúng ta học được nhiều thứ hơn, trước hết đó là một hệ nhị phân Golang, nghĩa là chúng ta cần bắt đầu trong hàm main.main. Ở đây, chúng tôi thấy sau một số tìm kiếm rằng nội dung liên quan đến cờ xảy ra trong một hàm được gọi là main.one được kiểm soát bằng một số so sánh:

hàm main.main



Tôi thực sự không biết so sánh là gì và thay vì bối rối trong việc kiểm tra nó, tôi nghĩ rằng tôi có thể thử và vá nó thay thế.

Để thực hiện việc này, tôi đã thay đổi hướng dẫn tại 0x00103f96 từ JNZ \(opcode 75\) thành JMP \(opcode 74\) với trình chỉnh sửa hex. Tôi đã lưu tệp nhị phân đã vá và chạy lại, hành vi sẽ thay đổi:



![](../../.gitbook/assets/image%20%2831%29.png)

Bây giờ nó muốn một mật khẩu. Tôi không biết mật khẩu mà nó mong đợi là gì nhưng sau khi xem xét xung quanh hàm main.one, tôi bắt gặp một so sánh khác:

![](../../.gitbook/assets/image%20%2834%29.png)

Sau một số thử nghiệm và gặp lỗi trong gdb, tôi xác nhận rằng mã đang tổng hợp các giá trị ascii của các ký tự của mật khẩu. Nếu tổng tổng các ký tự bằng 0x195 thì kiểm tra này thành công. Lưu ý bên dưới cách tôi lần đầu tiên nhìn thấy điều này. Khi tôi gửi mật khẩu A thì so sánh là 0x195 == 0x41?





```text
$ gdb ./patch1                                                                   
...
Reading symbols from ./patch1...
gdb-peda$ br *0x555555557a8b
Breakpoint 1 at 0x555555557a8b
gdb-peda$ r
Starting program: /root/grabcon/unknown2/patch1 

___.          .__                              
\_ |__ _____  |  | _____    ____   ____  ____  
 | __ \\__  \ |  | \__  \  /    \_/ ___\/ __ \ 
 | \_\ \/ __ \|  |__/ __ \|   |  \  \__\  ___/ 
 |___  (____  /____(____  /___|  /\___  >___  >
     \/     \/          \/     \/     \/    \/ 


Enter the password: 
A
...
[-------------------------------------code-------------------------------------]
   0x555555557a7d <main.one+1140>:      mov    rax,QWORD PTR [rax+0x8]
   0x555555557a81 <main.one+1144>:      cmp    QWORD PTR [rbp-0x48],rax
   0x555555557a85 <main.one+1148>:      jl     0x5555555579a6 <main.one+925>
=> 0x555555557a8b <main.one+1154>:      cmp    QWORD PTR [rbp-0x38],0x195
...

Thread 1 "patch1" hit Breakpoint 1, main.one () at med_re_2.go:30
30      med_re_2.go: No such file or directory.

gdb-peda$ x/1wx $rbp-0x38
0x7fffcf7aad58: 0x00000041
gdb-peda$
```

Để nhận một chuỗi ASCII có giá trị 0x195 \(405 thập phân\), tôi chỉ cần gửi char 50 \(ascii 2\) x 7 và char 55 \(ascii 7\) x 1:

```text
 22222227 = 0x195
```

Tôi đã chạy chương trình đã vá và nhập mật khẩu đó, không chắc chắn điều gì sẽ xảy ra:



Lấy Flag

```text
$ ./patch1                                                                                                                                                                               
___.          .__
\_ |__ _____  |  | _____    ____   ____  ____  
 | __ \\__  \ |  | \__  \  /    \_/ ___\/ __ \ 
 | \_\ \/ __ \|  |__/ __ \|   |  \  \__\  ___/ 
 |___  (____  /____(____  /___|  /\___  >___  >
     \/     \/          \/     \/     \/    \/ 

Enter the password: 
22222227 
Here ya go -> GrabCON{ 626c61636b647261676f6e }
```

