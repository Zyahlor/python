# 21 - 10 - 2026

## 1.DICTIONARY LÀ GÌ?
- dict - kiểu dữ liệu lưu thông tin theo cặp key:value
Ví dụ, lưu thông tin sinh viên:

```
user = { "name": "Bao","age": 19}
```

- `"name"` là key (khóa).
- `"Bao"` là value (giá trị).
- `"age"` là key.
- `19` là value.

Hãy tưởng tượng dictionary là một cuốn sổ: tìm theo tên mục (`key`) để lấy thông tin (`value`).
### 1.1 TRUY CẬP DỮ LIỆU

``` python
# lấy tên
print(user["name"]) # bao
# lấy tuổi
print(user["age"]) # 19
# lưu ý: phải dùng đúng key đã có, nếu viết sai sẽ báo keyerror
```
### 1.2 thêm dữ liệu

``` python
# thêm chiều cao:
user["height"] = 170
print(user) # {'name': 'Bao', 'age': 19, 'height': 170}
# nếu key chưa tồn tại, python sẽ thêm cặp mới
```
### 1.3 sửa dữ liệu
``` python
# đổi tuổi từ 19 -> 20
user["age"] = 20
print(user["age"]) # 20  
```

### 1.4 xóa dữ liệu

- có 2 cách
1.  `del`
``` python
del user["age"]
```
xóa key `"age"` cùng value 
2. `pop()`
``` python
user.pop("age")
```
Cũng xóa key `"age"`, đồng thời trả về value vừa bị xóa.
khác cái `del` là `pop()` có lưu giá trị xóa và xuất được 
Lưu ý: Nếu key không tồn tại, cả hai cách đều có thể gây lỗi.

### 1.5 `.get()` và `.keys`

1. `.get()` : lấy giá trị an toàn hơn
``` python
student = {"name": "An", "age": 18}

print(student.get("name"))    # An
print(student.get("score"))   # None
```
Khác với `student["score"]`, `.get("score")` không báo lỗi khi key chưa tồn tại.
có thể đặt giá trị mặc định
``` python
print(student.get("score", 0))  # 0
```
2. `.key()` : lấy danh sách các key
``` python
print(student.keys())
```
```
dict_keys(['name', 'age'])
```
### 1.6 `.values()` và `.items()`
1. `.values()` : lấy tất cả các giá trị 
``` python
print(user.values()) # "bao", 19
```
2. `.items()`:  lấy tất cả key và values
``` python
print(user.items()) #  { "name": "Bao","age": 19}
```
Đặc biệt:

```
for key, value in student.items():    print(key, value)
```

Kết quả:

```
name Bao
age 19
```

`items()` cho phép lấy cả key lẫn value trong mỗi vòng lặp, rất tiện khi xử lý dictionary.

### 1.7 ĐẾM TẦN SUẤT PHẦN TỬ TRONG LIST

- đây là ứng dụng thực tế của dictionary

Cho danh sách:
```
fruits = ["tao", "cam", "tao", "chuoi", "cam", "tao"]
```
Mục tiêu là tạo dictionary đếm số lần mỗi loại quả xuất hiện:
```
{    "tao": 3,    "cam": 2,    "chuoi": 1}
```
#### CÁC BƯỚC THỰC HIỆN:
``` python
# khởi tạo dict để lưu giá trị
count = {}
# khởi tạo 1 vòng lặp for
for key in fruits:
# tạo điều kiện nếu key ko có trong count thì gán nó làm key và giá trị = 1
	if key not in count:
		count[key] = 1
# nếu đã có thì sao? tăng giá trị đếm lên
    else:
	    count[key]+=1
# xuất thôi
print(count)
```