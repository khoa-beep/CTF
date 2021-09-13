# Basic RCE L01

HDD를 CD-Rom으로 인식시키기 위해서는 GetDriveTypeA의 리턴값이 무엇이 되어야 하는가

Đề bài yêu cầu ta là giá trị GetDriveTypeA là gì ?

Ta chạy thử chương trình

![](../../.gitbook/assets/image%20%2822%29.png)

![](../../.gitbook/assets/image%20%2823%29.png)

Vừa make me think your HD is a CD-Rom \( nghĩ HD của  bạn là CD-Rom \)

Và "this is not a CD-Rom Drver" \( Không phải là CD-ROM\), nghe nó có vẻ không phải :\( lúc đầu tôi hơi mơ hồ cho lắm nhưng thử load vào x64 DBG xem sao.

![](../../.gitbook/assets/image%20%2825%29.png)

Khi ta load vào ta thấy tại địa chỉ 0040102F có chuỗi hiện ra thông báo "this is not a CD-Rom Drver" 

Và câu lệnh đún nằm ở dưới địa chỉ 00402064 "Ok, I really think that your HD is a CD-ROM! :p"

Như vậy có liên quan đến phép toán so sánh cmp trên và lệnh je nhảy khi điều kiện 2 thanh ghi bằng nhau "cmp esi , eax"

![](../../.gitbook/assets/image%20%2821%29.png)

Đặt break ở địa chỉ  "00401000"

nhìn qua bên phải xem thanh ghi esi có giá trị 00401000 là điểm entrypoint của lệnh stack.

Ta có thể thấy được bên dưới lên inc esi thì có 1 lệnh tính toán như dec nó tính toán gì đó bên trong eax.

![](../../.gitbook/assets/image%20%2824%29.png)

Ta trance qua lệnh esi thì đến lệnh eax mà esi bây giời là 00401001 \( được cộng thêm 1 đơn vị\).

Ta tiếp trace qua tới câu lệnh so sánh

![](../../.gitbook/assets/image%20%2826%29.png)

Để ý thanh ghi eax mang giá trị 000000001 và esi mang gia trị 00401003 như vậy muốn câu lệnh này nhảy xuống thông báo tốt thì 2 thanh ghi phải bằng nhau.

Ok vậy chỗ khi gọi hàm "call GetDriveTypeA" 

Trước đó mình vẫn chưa hiểu giá trị trả về của hàm GetDriveTypeA. Thử search gg xem



| Return code/value | Description |
| :--- | :--- |
| **DRIVE\_UNKNOWN**0 |  The drive type cannot be determined. |
| **DRIVE\_NO\_ROOT\_DIR**1 |  The root path is invalid; for example, there is no volume mounted at the specified path. |
| **DRIVE\_REMOVABLE**2 |  The drive has removable media; for example, a floppy drive, thumb drive, or flash card reader. |
| **DRIVE\_FIXED**3 |  The drive has fixed media; for example, a hard disk drive or flash drive. |
| **DRIVE\_REMOTE**4 |  The drive is a remote \(network\) drive. |
| **DRIVE\_CDROM**5 |  The drive is a CD-ROM drive. |
| **DRIVE\_RAMDISK**6 |  The drive is a RAM disk. |

Sau khi tìm kiếm được thông tin trong bảng này thì 

