# 22 - 10 - 2026
## 1. FUNCTION  LÀ GÌ?
- là hàm  - 1 nhóm lệnh được đặt tên để mình có thể gọi ra khi cần

Ví dụ, bạn muốn cộng hai số. Không dùng function:
```
a = 3b = 5print(a + b)
```

Lần sau muốn cộng hai số khác, lại phải viết các lệnh tương tự.
- nếu dùng function?
``` python
def tong(a,b)
	return a+b
# than file
a,b = 5,6
print(tong(a,b))    # 11
print(tong(10,100)) # 110
```

Có 4 thứ bạn cần nhớ:

|Thành phần|Ý nghĩa|
|---|---|
|`def`|Khai báo hàm|
|`tong`|Tên hàm, bạn tự đặt|
|`a, b`|Parameter, biến nhận dữ liệu|
|`return`|Trả kết quả về nơi gọi hàm|
## 2. Parameter và Argument khác nhau thế nào?

- Parameter: biến được khai báo trong hàm để nhận dữ liệu.
- Argument: giá trị thực tế bạn truyền vào khi gọi hàm.
``` python
def tong(a, b):  # a, b là parameter
    return a + b

tong(3, 5)       # 3, 5 là argument
```

Cứ hiểu đơn giản: `a`, `b` là hai chiếc hộp, còn `3`, `5` là thứ bạn bỏ vào hộp.

## 3. function không return!

``` python
def xin_chao():
    print("Xin chao Bao!")

xin_chao()
# output
# Xin chao Bao!
```

Ở đây:

- `def xin_chao():` tạo hàm không cần nhận dữ liệu.
- `print()` in nội dung ra màn hình.
- `xin_chao()` gọi hàm để chạy các lệnh bên trong.

Lưu ý: `print()` là in ra màn hình, còn `return` là trả giá trị về cho chương trình. Hai thứ này không giống nhau.

## 4.scope trong python

- `scope` là phạm vi 1 biến có thể được truy cập
> có 2 loại: biến cực bộ - local scope, biến toàn cục - global scope

### 1. biến cực bộ

- chỉ sử dụng được trong function, tức nằm trong function nào thì chỉ có function đó sử dụng được

```python
def test():    
   x = 5    
   print(x)
   
test()       # 5
print(x)     # Lỗi: x không được định nghĩa ở bên ngoài
```

Biến `x` được tạo bên trong `test()`, nên bên ngoài không thể truy cập nó bằng tên `x`.

### 2. Global scope: phạm vi toàn cục

Biến được khai báo bên ngoài function nằm trong phạm vi toàn cục của module.

```python 
x = 10
def test():    
   y = 5    
   return y

print(test())  # 5
print(x)       # 10
```

- `x` là biến global.
- `y` là biến local.
- Function có thể đọc biến global nếu không bị che khuất bởi biến local cùng tên.

### 3. Nếu local và global trùng tên thì sao?

```python
x = 10
def test():    
   x = 5    
   return x

print(test())  # 5
print(x)       # 10
```

Hai biến `x` ở đây thuộc hai phạm vi khác nhau. Dòng `x = 5` bên trong hàm tạo một biến local mới, không thay đổi `x` bên ngoài.

So sánh với C++: bạn có thể gặp tình huống tương tự khi biến cục bộ che khuất biến bên ngoài cùng tên.

Ghi nhớ: Trong bài tập Python thông thường, hãy truyền dữ liệu qua parameter và trả kết quả bằng `return`, thay vì phụ thuộc vào biến global.

## 5. Default argument & Keyword argument

### 1. Default argument

- Khai báo giá trị mặc định cho parameter. Khi gọi hàm mà không truyền argument tương ứng, Python dùng giá trị mặc định đó.

``` python
def tinh_tien(gia, so_luong=1):
    return gia * so_luong

print(tinh_tien(100))     # 100
print(tinh_tien(100, 3))  # 300
```
- `gia`: parameter bắt buộc.
- `so_luong=1`: parameter có giá trị mặc định.
- `tinh_tien(100)`: không truyền `so_luong`, nên mặc định là `1`.
- `tinh_tien(100, 3)`: truyền `3`, nên giá trị mặc định bị thay thế.

Quy tắc: Parameter không có giá trị mặc định bắt buộc phải đứng trước parameter có giá trị mặc định.
Không viết `def f(a=10, b):` vì sẽ gây lỗi cú pháp.

### 2. Keyword argument

- thay vì truyền theo vị trí, chỉ rõ tên của tham số (parameter)
``` python
def thong_tin(name, age, city):
    return f"{name}, {age}, {city}"

print(thong_tin("Bao", 20, "HCM"))
print(thong_tin(city="HCM", name="Bao", age=20))
```

Hai lời gọi trên cho kết quả giống nhau.
- Positional argument: `"Bao"` được gán cho `name` theo vị trí.
- Keyword argument: `city="HCM"` chỉ rõ giá trị dành cho `city`.
Keyword argument hữu ích khi hàm có nhiều parameter, vì không cần nhớ thứ tự của tất cả chúng.

### 3. Kết hợp cả hai

```python 
def tao_tai_khoan(username, role="user", active=True):
    return {
        "username": username,
        "role": role,
        "active": active
    }

print(tao_tai_khoan("bao"))
print(tao_tai_khoan("bao", role="admin"))
print(tao_tai_khoan("bao", active=False, role="user"))
```

Kết quả lần lượt:

```
{"username": "bao", "role": "user", "active": True}
{"username": "bao", "role": "admin", "active": True}
{"username": "bao", "role": "user", "active": False}
```

Lưu ý: `username` là bắt buộc. `role` và `active` có giá trị mặc định nhưng có thể được ghi đè bằng positional hoặc keyword argument.