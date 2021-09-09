# x64 DBG

## Introduction

  **x64dbg** là giải pháp khử lỗi ứng dụng tích hợp nhiều tính năng hỗ trợ các nhà phát triển ứng dụng tối đa trong công việc viết và lập trình ứng dụng. Bên cạnh đó, phần mềm x64dbg còn có giao diện dễ sử dụng, cung cấp các tiện ích hỗ trợ, và cho phép người dùng cấu hình các thông số qua trình đơn Settings chuyên nghiệp.

```cpp
// hello-world.cpp

#include <stdio.h>

void main(){

    puts("hello world!\n");

}
```

Ta sẽ đảo ngược nó từ mã máy sang code 

Link tải phần mền debug : [https://x64dbg.com/\#start](https://x64dbg.com/#start)

![](../../.gitbook/assets/41eef0c3d834857510dcebd8a7d454edfc43fe1cfec6a75ff04bf63cf9f1d001.png)

Chọn vào x96 vào run.

![](../../.gitbook/assets/55ba8889991f32648162dc616e0a1d845ac5f5ba3ce1bbabf45fb9f2308edaa4.png)

giao diện x64dbg 

Cách sử dụng x64dbg - Giao diện người dùng cơ bản

![](../../.gitbook/assets/41597e027fd15888321f6a0d9f1c0ddece781475429bb87b6b5c6f2b688d098f.png)

1       Mở File chương trình cần phân tích

2      Reset lại chương trình

3      Ngừng chương trình 

4      Chạy tiếp chương trình

5      Tạm dừng chương trình. Nó được sử dụng khi bạn muốn tự ý dừng lại khi đang chạy.

6      Thực thi một dòng mã lắp ráp. Nếu bạn cố gắng thực hiện lệnh gọi, nó sẽ đi vào bên trong hàm      được gọi. \(Bước vào\)

7     Thực thi một dòng mã lắp ráp. Nếu bạn cố gắng thực hiện cuộc gọi, nó sẽ chạy cho đến khi hàm gọi thực hiện lệnh ret \(cho đến khi nó trả về\) và sau đó dừng lại. \(Bước qua\)



Một số giao diện chú ý 

![](../../.gitbook/assets/00a0b58f93f76db74aef035ed244c4bfd4da69a5f75c876876f5a1564573a143.png)

Hình 1 Hiển thị ta thấy đươc vài mã lắp ráp bao gồm địa chỉ

Hình 2  Hiển thị các thanh ghi trong CPU

Hình 3 Phần này ta xem chi tiết trong Hình 1

Hình 4

 Nó hiển thị các giá trị rcx, rdx, r8, r9 trong số trạng thái thanh ghi hiện tại. Lý do tại sao nó được hiển thị riêng biệt với cửa sổ 2 là vì thứ tự thanh ghi là thứ tự đối số của quy ước gọi hàm được sử dụng theo mặc định trong hệ điều hành Windows 64-bit. Điều này cho phép bạn dễ dàng kiểm tra những giá trị nào được truyền dưới dạng đối số trong lệnh gọi.

Hình 5 

Hiển thị giá trị hex. Nó không tự động hiển thị theo quá trình thực thi của chương trình, và nếu bạn đưa ra lệnh để xem giá trị hex trong cửa sổ khác, nó sẽ được hiển thị trong cửa sổ này.

Hình 6

Hiển thị giá trị ngăn xếp. Theo mặc định, nó được hiển thị theo giá trị rsp. Đường màu xanh lam ở giữa thể hiện vùng ngăn xếp cho một chức năng. Tuy nhiên, nó đôi khi không chính xác vì x64dbg đoán và hiển thị nó thông qua phương pháp heuristic.



## Cách đặt break Point tại điểm bất kì để Debug phần mền

![](../../.gitbook/assets/27b9d231cb5e9b309df03ec29b75da01a34226a79cf146e56b67dff5a6f250e7.png)

Ta click chuột phải và chọn Breakpoint or là ta có thể nhần f2 luôn tại chỉ ta đặt điểm dừng

![](../../.gitbook/assets/f02d1b76c789488e01d37dc349bba482cfb9cba04abca038e48e513d4f1cd853.png)

Một số trường hợp khác ta có thể vào tab Breakpoint list và ta có thể tùy chọn như thêm xóa or thay đổi



## Note

Hình ảnh trên là bản x64dbg Hàn quốc nên các bạn có thể tìm đến link này để tìm hiểu thêm về cách dùng phần mền này

[https://error4hack.com/x64dbg-tutorial/](https://error4hack.com/x64dbg-tutorial/)











