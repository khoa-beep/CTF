# vault-door-3

Author: Mark E. Haase

**Description**

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/943ea40e3f54fca6d2145fa7aadc5e09/VaultDoor3.java)

Thử thách này tương tự như trước cũng mở source lên phân tích.

```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}

```

Phân tích sơ bộ thì ở trên này có lẽ tính toán gì đó rồi lưu vào buff xong rồi convert thành chuỗi so sánh bằng với chuỗi "jU5t\_a\_sna\_3lpm18g947\_u\_4\_m9r54f".

## Hint&#x20;

Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

Đề bài có ý tưởng là dùng lại vòng lặp lưu vào buff như trên kia ta code lại python xem.

```python
flag_en = "jU5t_a_sna_3lpm18g947_u_4_m9r54f"
result = []
for i in range(len(flag_en)):
	result.append(0)

for i in range(31,16,-2):
	result[i] = flag_en[i]

for i in range(0,8,1):
	result[i] = flag_en[i]

for i in range(8,16,1):
	result[23-i] = flag_en[i]

for i in range(16,32,2):
	result[46-i] = flag_en[i]

print("picoCTF{{{}}}".format(''.join(result)))
```

Run nào .

picoCTF{jU5t\_a\_s1mpl3\_an4gr4m\_4\_u\_79958f}

