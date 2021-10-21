# vault-door-4

Author: Mark E. Haase

**Description**

This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/c695ee23309d453a3ef369c34cc1bccb/VaultDoor4.java)



Mở code phân tích như ban đầu.

```java
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
            '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}

```

Hint

Use a search engine to find an "ASCII table".

You will also need to know the difference between octal, decimal, and hexadecimal numbers.

```python
passBytes = [None] * 32
myBytes = [
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            '0x55', '0x6e', '0x43', '0x68', '0x5f', '0x30', '0x66', '0x5f',
            '0o142', '0o131', '0o164', '0o63' , '0o163', '0o137', '0o70' , '0o146' ,
            '4' , 'a' , '6' ,'c' , 'b' , 'f' , '3' , 'b',
	]

# base10
for i in range(0,8):
	passBytes[i] =  chr(myBytes[i])

# base16
for i in range(8,16):
	#passBytes[i] =  bytearray.fromhex(myBytes[i].replace('0x', '')).decode()
	passBytes[i] =  chr(int(myBytes[i], 16))

# base8
for i in range(16,24):
	passBytes[i] =  chr(int(myBytes[i], 8))

for i in range(24,32):
	passBytes[i] =  myBytes[i]

print("picoCTF{{{}}}".format(''.join(passBytes)))// Some code
```

flag : picoCTF{jU5t\_4\_bUnCh\_0f\_bYt3s\_8f4a6cbf3b}
