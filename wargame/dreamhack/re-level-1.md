---
description: 'https://dreamhack.io/wargame/challenges/15/'
---

# Re Level 1

Solution

Từ level 0 trên ta làm tương tự

![](../../.gitbook/assets/0%20%282%29.png)

Kiểm tra phân tích tĩnh bằng IDA và đặt tên hàm theo đúng chương trình

Vào hàm Check xem có gì

if \( \*a1 != 67 \)

 return 0i64;

 if \( a1\[1\] != 111 \)

 return 0i64;

 if \( a1\[2\] != 109 \)

 return 0i64;

 if \( a1\[3\] != 112 \)

 return 0i64;

 if \( a1\[4\] != 97 \)

 return 0i64;

 if \( a1\[5\] != 114 \)

 return 0i64;

 if \( a1\[6\] != 51 \)

 return 0i64;

 if \( a1\[7\] != 95 \)

 return 0i64;

 if \( a1\[8\] != 116 \)

 return 0i64;

 if \( a1\[9\] != 104 \)

 return 0i64;

 if \( a1\[10\] != 101 \)

 return 0i64;

 if \( a1\[11\] != 95 \)

 return 0i64;

 if \( a1\[12\] != 99 \)

 return 0i64;

 if \( a1\[13\] != 104 \)

 return 0i64;

 if \( a1\[14\] != 52 \)

 return 0i64;

 if \( a1\[15\] != 114 \)

 return 0i64;

 if \( a1\[16\] != 97 \)

 return 0i64;

 if \( a1\[17\] != 99 \)

 return 0i64;

 if \( a1\[18\] != 116 \)

 return 0i64;

 if \( a1\[19\] != 51 \)

 return 0i64;

 if \( a1\[20\] == 114 \)

 return a1\[21\] == 0;

 return 0i64;

Ta thấy một mảng a chứa tổng số lượng phần tử là 21 và nó đem từng ký tự tường vị trí so sanh với 1 số thập phân thì ta thử convert sang ký tự được

Flag : Compar3\_the\_ch4ract3r

![](../../.gitbook/assets/1%20%283%29.png)

