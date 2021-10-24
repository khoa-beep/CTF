# ANATOMY OF A BINARY

### Introduction

Máy tính hiện đại thực hiện các phép tính của chúng bằng cách sử dụng hệ thống số nhị phân, hệ thống này biểu thị tất cả các số dưới dạng chuỗi số đơn vị và số không. Các mã máy mà các hệ thống này thực thi được gọi là mã nhị phân. Mỗi chương trình bao gồm một tập hợp mã nhị phân (hướng dẫn máy) và dữ liệu (biến, hằng số và những thứ tương tự). Để theo dõi tất cả các chương trình trên một hệ thống nhất định, bạn cần một cách để lưu trữ tất cả mã và dữ liệu thuộc mỗi chương trình trong một tệp độc lập. Bởi vì những tập tin này chứa các chương trình nhị phân có thể thực thi, chúng được gọi là các tệp thực thi nhị phân, hoặc chỉ đơn giản là nhị phân. Phân tích các mã nhị phân này là mục tiêu của chương  này.

1.1 The C Compilation Process ( quy trình dịch ngược c++ or c )

Binary được tạo ra thông qua quá trình biên dịch, là quá trình dịch mã nguồn mà con người có thể đọc được, chẳng hạn như C hoặc C ++, thành mã máy bộ xử lý của bạn có thể thực thi.&#x20;

1 Hình 1-1 cho thấy các bước liên quan đến một quy trình biên dịch mã C (các bước biên dịch C ++ tương tự). Biên dịch mã C bao gồm bốn giai đoạn, một trong số đó (đủ khó xử) là cũng được gọi là biên dịch, giống như quá trình biên dịch đầy đủ.&#x20;

Các giai đoạn là **preprocessing, compilation, assembly, and linking**. Trong thực tế, các trình biên dịch hiện đại thường hợp nhất một số hoặc tất cả các giai đoạn này, nhưng với mục đích trình diễn, tôi sẽ bao gồm tất cả chúng một cách riêng biệt

![](<../.gitbook/assets/image (41).png>)

1.1.1 The Preprocessing Phase ( Tiền xử lý )

Quá trình biên dịch bắt đầu với một số nguồn mà bạn muốn để biên dịch (được hiển thị từ ﬁle-1.c đến ﬁle-n.c trong Hình 1-1).&#x20;

Có thể chỉ có một nguồn duy nhất, nhưng các chương trình lớn thường bao gồm nhiều ﬁle hơn nữa.&#x20;

Điều này không chỉ làm cho dự án dễ quản lý hơn mà còn tăng tốc độ biên dịch bởi vì nếu một trong những thay đổi, bạn chỉ phải biên dịch lại hơn là tất cả các mã.&#x20;

Nguồn C ﬁle chứa macro (ký hiệu là #define) và #include direc- tives. Bạn sử dụng các chỉ thị #include để bao gồm header ﬁle (với exten- sion .h) mà nguồn phụ thuộc vào. Giai đoạn tiền xử lý mở rộng mọi lệnh #define và #include trong nguồn ﬁle vì vậy tất cả những gì còn lại là C thuần túy mã đã sẵn sàng để được biên dịch. Hãy làm cho điều này cụ thể hơn bằng cách xem một ví dụ. Ví dụ này sử dụng trình biên dịch gcc, là trình biên dịch mặc định trên nhiều bản phân phối Linux.

Ví dụ về đoạn mã này.

```
#include <stdio.h>
#define FORMAT_STRING "%s"
#define MESSAGE "Hello, world!\n"
int
main(int argc, char *argv[]) {
printf(FORMAT_STRING, MESSAGE);
return 0;
}
```

Trong giây lát, bạn sẽ thấy điều gì xảy ra với điều này trong phần còn lại của quá trình biên dịch, nhưng hiện tại, chúng tôi sẽ chỉ xem xét đầu ra của phần trước giai đoạn xử lý. Theo mặc định, gcc sẽ tự động thực hiện tất cả quá trình biên dịch các giai đoạn, vì vậy bạn phải yêu cầu rõ ràng nó dừng lại sau khi xử lý trước và hiển thị bạn là đầu ra trung gian. Đối với gcc, điều này có thể được thực hiện bằng lệnh gcc -E -P, trong đó -E yêu cầu gcc dừng lại sau khi xử lý trước và -P gây ra trình biên dịch để bỏ qua thông tin gỡ lỗi để đầu ra sạch hơn một chút. Liệt kê 1-2 hiển thị đầu ra của giai đoạn tiền xử lý, được chỉnh sửa cho ngắn gọn. Khởi động VM và làm theo để xem toàn bộ đầu ra của bộ tiền xử lý.

```
$ gcc -E -P compilation_example.c
typedef long unsigned int size_t;
typedef unsigned char __u_char;
typedef unsigned short int __u_short;
typedef unsigned int __u_int;
typedef unsigned long int __u_long;
/* ... */
extern int sys_nerr;
extern const char *const sys_errlist[];
extern int fileno (FILE *__stream) __attribute__ ((__nothrow__ , __leaf__)) ;
extern int fileno_unlocked (FILE *__stream) __attribute__ ((__nothrow__ , __leaf__)) ;
extern FILE *popen (const char *__command, const char *__modes) ;
Anatomy of a Binary 13extern int pclose (FILE *__stream);
extern char *ctermid (char *__s) __attribute__ ((__nothrow__ , __leaf__));
extern void flockfile (FILE *__stream) __attribute__ ((__nothrow__ , __leaf__));
extern int ftrylockfile (FILE *__stream) __attribute__ ((__nothrow__ , __leaf__)) ;
extern void funlockfile (FILE *__stream) __attribute__ ((__nothrow__ , __leaf__));
int
main(int argc, char *argv[]) {
printf(Ê"%s", Ë"Hello, world!\n");
return 0;
}
```



**1.1.2 The Compilation Phase ( Giai đoạn tổng hợp )**

Sau khi giai đoạn tiền xử lý hoàn tất, nguồn đã sẵn sàng để kết nối chất đống. Giai đoạn biên dịch lấy mã được xử lý trước và dịch nó sang hợp ngữ. (Hầu hết các trình biên dịch cũng thực hiện tối ưu hóa nặng trong giai đoạn này, thường được coi là mức tối ưu hóa thông qua lệnh chuyển đổi dòng chẳng hạn như tùy chọn -O0 đến -O3 trong gcc.

![](<../.gitbook/assets/image (42).png>)

