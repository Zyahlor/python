# 24 - 08 - 2026
# variable

## 1. variable là gì?
`variable` là 1 biên khởi tạo từ  chương trình của 1 ngôn ngữ lập trình, khởi tạo được gọi là khai báo , sau khi khai báo hệ điều hành sẽ cấp bộ nhớ cho biến đó thuộc ngôn ngữ c/c++

còn trên python, nó được xem là 1 đối tượng (object)

object là 1 giá trị, dữ liệu tồn tại trong bộ nhớ, python quản lý nó như là 1 thực thể có thông tin riêng


vd: 

n = 10

python sẽ tạo ra 1 object `10`, n sẽ tham chiếu tới cái object `10`

> trong python ,  mọi thứ là object

``` python
n = 10              # int
name = "bao"          # string
age = int(input(" nhap tuoi cua ban: "))  #input
pi = 3.14           # float
student = True      # boolean
```

cách kiểm tra kiểm dữ liệu của 1 object nào đó trong python ,  chúng ta dùng `type(ten_bien)`

``` python
print(type(n))      # output: <class 'int'>
print(type(name))   # output: <class 'str'>
```
## 2. những điều hay ho

### 1.  python xác định theo  kiểu runtime

kiểu của biến ko được ktra hay gán cứng khi biên dịch, được quyết định dựa vào giá trị biến đó
trỏ tới object 
> khác vs c/c++ là ngôn ngữ biên dịch, python,js là ngôn ngữ thông dịch, không cần phải tạo ra file nhị phân thực thi để chạy chương trình

`python` ko cần khai báo kiểu dữ liệu ra như c/c++ 

```python
x = 10
name = "bao"
```

```c/c++
int x = 10;
string name = "bao"
```
### 2. tự do gán biến
có thể gán lại kiểu dữ liệu khác ban đầu

vd:

x = 10  # int

x = "bao" # string

### 3.gán nhiều biến
a = 10
b = 20

=> a,b = 10,20
