# 22 - 10 - 2026
## 1. FILE LÀ GÌ ĐỐI VỚI PYTHON?
Giả sử bạn có file `data.txt` chứa nội dung:

```
Hello Python
Hoc lap trinh
Dong thu ba
```

Python có thể mở file để đọc nội dung, giống như bạn mở Notepad để xem văn bản.
Có 3 việc khác nhau:
- `open()`: mở file.
- `read()`: đọc nội dung file.
- `close()`: đóng file sau khi dùng xong.
Ví dụ đầu tiên:
```python
f = open("data.txt", "r")
data = f.read()
print(data)
f.close()
```

Giải thích từng dòng:

|Code|Ý nghĩa|
|---|---|
|`open("data.txt", "r")`|Mở file để đọc|
|`f`|Biến giữ đối tượng file|
|`f.read()`|Đọc toàn bộ nội dung|
|`data`|Biến chứa nội dung vừa đọc|
|`f.close()`|Đóng file|

Ở đây, `"r"` là chế độ read, tức đọc file.

## 2. dùng  `with open()` để làm gì?
Trong Python, người ta thường viết:

```python 
with open("data.txt", "r") as f:
    data = f.read()

print(data)
```

Đừng lo, ta chỉ cần hiểu 2 điều:
- `as f`: đặt tên `f` cho file đang mở.
- `with`: tự đóng file khi ra khỏi khối lệnh, kể cả khi có lỗi trong quá trình xử lý.
Dòng có `with` kết thúc bằng `:` nên dòng bên dưới phải thụt vào.
Từ giờ, hãy ưu tiên dùng `with open(...)`. Bạn không cần tự nhớ đóng file nữa.

## 3. ĐỌC TỪNG DÒNG TRONG FILE

Giả sử `data.txt` có nội dung:

```
Apple
Banana
Orange
```

### 1. `readline()` là gì?

`readline()` đọc một dòng mỗi lần gọi.

``` python
with open("data.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()

print(line1)
print(line2)
```
Kết quả:
```
Apple

Banana
```

Tại sao có dòng trống? Vì `readline()` thường giữ lại ký tự xuống dòng `\n` ở cuối mỗi dòng, còn `print()` cũng tự xuống dòng. Hai lần xuống dòng tạo ra khoảng trống đó.

Hãy hình dung file có một con trỏ đang đứng ở đầu file. Mỗi lần gọi `readline()`, con trỏ tiến đến dòng tiếp theo.

### 2. `readlines()` là gì?

`readlines()` đọc tất cả các dòng và trả về một list chứa các chuỗi.

```python
with open("data.txt", "r") as f:    
   lines = f.readlines()
print(lines)
```
Kết quả:
```
['Apple\n', 'Banana\n', 'Orange']
```
So sánh nhanh:

| Hàm           | Kết quả                     |
| ------------- | --------------------------- |
| `read()`      | Một chuỗi chứa toàn bộ file |
| `readline()`  | Một chuỗi chứa một dòng     |
| `readlines()` | Một list chứa các dòng      |
## 3. ĐẾM SỐ DÒNG
File `data.txt`:

```
Apple
Banana
Orange
Grape
```

Code:

```PYTHON
with open("data.txt", "r") as f:    
    lines = f.readlines() # lines =["apple\n","banana\n","orange\n","grape\n"]
    count = len(lines)
print(count)
```
Kết quả:
```
4
```

Có đúng 3 thao tác:
1. `f.readlines()` lấy các dòng và lưu vào list `lines`.
2. `len(lines)` đếm số phần tử trong list.
3. `print(count)` in số dòng ra màn hình.

## 4. GHI DỮ LIỆU

``` python
with open("file.txt","w")as f:
 f.write("hello")
```

Chạy xong, Python sẽ tạo file `output.txt` nếu file chưa tồn tại, rồi ghi nội dung vào.
Có hai chế độ cần nhớ:

|Chế độ|Ý nghĩa|
|---|---|
|`"r"`|Đọc file|
|`"w"`|Ghi file, xóa nội dung cũ nếu file đã tồn tại|

Cẩn thận: `"w"` sẽ xóa nội dung cũ khi mở file. Đừng thử trên file chứa dữ liệu quan trọng.

### Thử thay đổi nội dung

```
with open("output.txt", "w") as f:    f.write("Apple\n")    f.write("Banana\n")    f.write("Orange\n")
```

Kết quả trong `output.txt`:

```
Apple
Banana
Orange
```

`\n` là ký tự xuống dòng. Nếu không có nó, nội dung sẽ dính liền thành `AppleBananaOrange`.

## 5. TÌM KIẾM TỪ TRONG FILE
Tạo file `log.txt` với nội dung:
```
User Bao login success
User An login failed
User Minh login success
User Bao login failed
```
Yêu cầu: Viết chương trình tìm xem từ `"failed"` xuất hiện trong những dòng nào.

Kết quả mong muốn:
```
User An login failed
User Bao login failed
```

Ta cần thực hiện 3 bước:
1. Mở file và đọc từng dòng.
2. Kiểm tra dòng hiện tại có chứa `"failed"` hay không.
3. Nếu có, in dòng đó ra.

Bạn đã biết `with open()`, `readlines()` và vòng lặp `for`. Hôm nay chỉ cần ghép chúng lại.

Ví dụ kiểm tra một chuỗi:

```PYTHON
line = "User An login failed"

if "failed" in line:
    print(line)
```

Kết quả:

```
User An login failed
```

Điều kiện `"failed" in line` kiểm tra xem chuỗi `line` có chứa từ `"failed"` hay không.

``` python
# neu khong thich phan biet hoa - tuong
# demo 
keyword = input("nhap tu khoa:").lower()
for line in log_line:
    if keyword in line.lower():
        print(line.strip())
```










##  MỞ RỘNG

#### `f.seek(0)`

Khi mở file, Python có một con trỏ đọc file, cho biết vị trí đang đọc đến đâu.

```python
with open("programming.txt", "r") as f:
    data = f.read()  # Đọc hết file, con trỏ đến cuối
    f.seek(0)        # Đưa con trỏ về đầu file
    lines = f.readlines()  # Đọc lại tất cả các dòng

print(data)
print(lines)
```

Kết quả:

```
c++
python
networking

['c++\n', 'python\n', 'networking\n']
```

- `f.read()`: đọc hết nội dung, con trỏ đi đến cuối file.
- `f.seek(0)`: đưa con trỏ về vị trí `0`, tức đầu file.
- `f.readlines()`: đọc tất cả các dòng từ vị trí hiện tại.
#### `NỐI NỘI DUNG FILE`

- chúng ta biết `w` là ghi nội dung vô file **nhưng** nó sẽ bị **xóa** các nội dung cũ
- chúng ta cần thêm nội dung mà ko bị xóa nội dung cũ
- chúng ta có tham số `a`
#### Phân biệt `"w"` và `"a"`

|Chế độ|Tác dụng|
|---|---|
|`"r"`|Đọc file|
|`"w"`|Ghi mới, xóa nội dung cũ|
|`"a"`|Ghi nối tiếp vào cuối file|
#### Ví dụ thực tế

Giả sử `data.txt` đang có:

```
Python
C++
```

Dùng `"a"` để thêm nội dung:

```python
with open("data.txt", "a") as f:    
  f.write("Networking\n")
```

Sau khi chạy, file sẽ thành:

```
Python
C++
Networking
```

Chạy đoạn code trên lần nữa, `Networking` sẽ được thêm một lần nữa vào cuối file.

#### Một lưu ý nhỏ

Nếu dùng `"a"` mà không có `\n`, nội dung mới có thể dính vào cuối dòng cũ.

Ví dụ:

```python
with open("data.txt", "a") as f:    
 f.write("Networking")
```

Nếu file kết thúc bằng `C++` và không có ký tự xuống dòng, kết quả có thể là:

```
Python
C++Networking
```

Vì vậy, hãy chú ý ký tự `\n` khi ghi thêm dữ liệu.