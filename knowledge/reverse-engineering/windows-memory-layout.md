# Windows Memory Layout

#### **Giới thiệu khóa học 📋**

Bố trí bộ nhớ đề cập đến cấu hình của bộ nhớ ảo quá trình. Khi bạn chạy một chương trình, hệ điều hành sẽ phân bổ không gian bộ nhớ khả dụng cho tiến trình. Trong khoa học máy tính, không gian này được gọi là bộ nhớ ảo.

Hệ điều hành đề cập đến thông tin của chương trình để dữ liệu được lưu trữ trong chương trình được lưu trữ trong khu vực thích hợp.

Nó phân vùng bộ nhớ ảo được quy trình sử dụng theo mục đích và lưu trữ dữ liệu được quy trình sử dụng trong phân vùng thích hợp. Bằng cách nhóm các dữ liệu tương tự nhau, hệ điều hành có thể cung cấp cho mỗi ngăn các quyền thích hợp và các nhà phát triển có thể hiểu bộ nhớ của quy trình một cách trực quan hơn.

Chìa khóa của kỹ thuật đảo ngược phần mềm là phân tích hệ nhị phân để hiểu hành vi của nó. Tuy nhiên, như chúng ta đã học trong Nền tảng: Kiến trúc Máy tính, hành vi của một hệ nhị phân có liên quan rất chặt chẽ đến bộ nhớ. Do đó, để hiểu chi tiết hành vi của một nhị phân, cần phải hiểu bộ nhớ mà nhị phân tương tác với nó.

Trong khóa học này, mình sẽ giải thích những điều cơ bản về bố trí bộ nhớ trong quy trình Windows.

Tổng quan ✔️

* .text
* .data
* .rdata



```cpp
int main() { return 31337; }
```

### Text

Phần .text là nơi chứa mã máy thực thi.

Bởi vì chương trình phải có khả năng thực thi mã để nó hoạt động, phân đoạn này được cấp quyền đọc và thực thi. Mặt khác, hầu hết các hệ điều hành hiện đại đều loại bỏ quyền ghi vào phân đoạn này, vì việc có quyền ghi sẽ khiến kẻ tấn công dễ dàng tiêm mã độc hơn.

Khi hàm main, trả về số nguyên 31337 bên dưới, được biên dịch, nó được chuyển đổi thành mã máy 554889e5b8697a00005dc3, được đặt trong đoạn mã.



```cpp
int data_num = 31337;

char data_rwstr[] = "writable_data";        // data

int main() { ... }

```

### 

### rdata

```cpp
const char data_rostr[] = "readonly_data";

char *str_ptr = "readonly";  // str_ptr은 .data, 문자열은 .rdata

int main() { ... }
```

Phần .rdata lưu trữ các hằng số toàn cục có giá trị được đặt tại thời điểm biên dịch, cũng như thông tin về DLL và các hàm bên ngoài được tham chiếu. CPU cần có khả năng đọc dữ liệu trong phần này, do đó, quyền đọc được cấp, nhưng không được ghi.

Dưới đây là các loại dữ liệu khác nhau có trong phần .rdata. Một biến cần chú ý là str\_ptr. str\_ptr trỏ đến chuỗi “readonly”, str\_ptr là một biến toàn cục, nằm trong .data, nhưng “readonly” được coi là một chuỗi không đổi và được đặt trong .rdata.

Trước đây, thông tin của các tệp DLL và các chức năng bên ngoài được tham chiếu được lưu trữ trong phần .idata, nhưng gần đây nhất, nó được lưu trữ trong phần .rdata.

