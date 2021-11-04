---
description: >-
  Chúng ta đã được tiếp cận đến những bài tập Java cơ bản ở những bài viết
  trước. Tại bài viết này mình sẽ chia sẻ thêm cho các bạn những bài tập OOP
  Java cơ bản cho những người mới tiếp cận với khái ni
---

# JAVA OOP

### Bài tập OOP Java cơ bản có lời giải





Bài tập 1:

*   Viết một chương trình khai báo một lớp Rectangle có 2 thuộc tính là chiều dài và chiều rộng và có các phương thức sau:

    * &#x20;Hàm tạo không tham số.
    * Hàm tạo có 2 tham số.
    * Get/set cho các thuộc tính.
    * Phương thức tính diện tích hình chữ nhật.
    * Phương thức tính chu vi hình chữ nhật.



    Bài tập 2:

    * Viết chương trình khai báo một lớp Phương trình bậc 2 với các thuộc tính là a, b, c với các phương thức sau:
      * Hàm tạo không tham số.
      * Hàm tạo có 3 tham số.
      * Get/set cho 3 thuộc tính.
      * Phương thức tính delta.
      * Phương thức tính nghiệm phương trình.

    Bài tập 3:

    * Viết chương trình khai báo một lớp trừu tượng là Animal có phương thức eat() và makeSound().
    *   Xây dựng các lớp Cat và Bird kế thừa lớp Animal trong đó:

        * Lớp Cat có phương thức run()
        * Lớp Bird có phương thức fly()



    ## Solution&#x20;



Bài 1

```java
package Baitapoop;

public class Rectangle {
    private double weight;
    private double height;

    public Rectangle(double weight, double height) {
        this.weight = weight;
        this.height = height;
    }

    public Rectangle() {
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

     public double getArea() { // Diện tích hình chữ nhật
        return this.weight * this.height;
    }

    public double getPerimeter() { //Chu vi hình chữ nhật
        return (this.height + this.weight) * 2;
    }


}

```



```java
// Some codepackage Baitapoop;

public class File_Run<main> {
    public static void main(String[] args) {
        // khoi tao object
        Rectangle re = new Rectangle(20.22,11.0);
        System.out.println("Dien tich hinh chu nhat : " + re.getArea()); // su dung "." de truy cap phuong thuc
        System.out.println("Chu vi : " + re.getPerimeter());

    }
}
```

