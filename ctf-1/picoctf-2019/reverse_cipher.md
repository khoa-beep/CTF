# reverse\_cipher

Author: Danny Tunitis

**Description**

We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev\_this). Can you reverse the flag.

Tại câu hỏi này đề bài cho ta 1 file có chứa flaf ( mà nó ko đúng )

file thứ 2 là elf nhị phân linux

Ta mở vào IDA và f5 xem chương trình là gì.

![](<../../.gitbook/assets/image (41) (1).png>)

Hàm này sẽ có các nhiệm vụ sau :

* Mở file _flag.txt_ để đọc flag và mở file _rev\_this_ để ghi kết quả
* Ở ô tô đỏ đầu tiên, sẽ ghi 8 kí tự đầu vào file _rev\_this_
* Ở ô tô đỏ thứ hai, sẽ duyệt từ kí tự thứ 8 đến kí tự thứ 22

\+ Nếu vị trí chứa kí tự là lẻ, thì thực hiện trừ kí tự đó cho 2

\+ Nếu vị trí chứa kí tự là chẵn, thì thực hiện cộng kí tự đó cho 5

\+ Kết quả lưu vào file rev\_this



Code python

```python
flag = "picoCTF{w1{1wq84fb<1>49}"
c = ""
for i in range(0,8,1):
	c += flag[i]
for i in range(8,23,1):
	if(i % 2 == 0):
		c += chr(ord(flag[i]) - 5)
	else:
		c += chr(ord(flag[i]) + 2)
for i in range(23,len(c),1):
	c+=flag[i]
print(c)
```

picoCTF{r3v3rs36ad73964}
