# 20 - 09 - 2026
# `SET`
## 1. `set` là gì?
- là tập hợp các phần tử không trùng nhau.
```python
ports = {22, 80, 443, 80, 22}

print(ports) # output: {80,443,22} -> tự loại bỏ phần tử trùng
```
- so sánh với list:
```python
ports_list = [22, 80, 443, 80, 22]
ports_set = {22, 80, 443, 80, 22}

print(ports_list) # output :[22, 80, 443, 80, 22]
print(ports_set)  # output :{22,80,443}
```
## 2. `Set` không có index !
Khác với tuple/list có thể lấy phần từ = index như `ds[0]`, `ds[1]`,....
set không thể làm như vậy
``` python
ports = {22, 80, 443}

ports[0]    # ❌
ports[-1]   # ❌

# cách đúng:
80 in ports # -> true
53 in ports # -> false
```
## 3. thêm/xóa
thao tác cơ bản:
- `add()` : thêm phân tử
``` python
ports = {22, 80, 443}

ports.add(53) # {53,22,80,443}
```
- `update`:thêm nhiều phần tử
``` python
ports = {22,80,443}
ports.update([21,25,110]) # output {21,25,110,22,80,443}
```
- `remove()`: xóa phần tử
``` python
ports = {22,80,443}
ports.update([21,25,110]) # output {21,25,110,22,80,443}

ports.remove(21) # output {25,110,22,80,443}
# nếu không có phần tử trong set -> báo lỗi
```
- `discard`: cũng là xóa nhưng nếu phần tử không tồn tại không báo lỗi
## 4. `Union` & `Intersection`
Đây là phần đặc trưng của set

1. `Union` (`|`) là gì?
- Lấy tất cả phần tử của 2 set, loại trùng:

```python
scan1 = {1,2,3,4}
scan2 = {3,4,5,6}

scan3 = scan1 | scan2 # output = {1,2,3,4,5,6}
# hoặc có thể dùng method:
scan3 = scan1.union(scan2)

```

2. `Intersection` (`&`) là gì?
- Lấy phần tử xuất hiện trong cả 2

``` python
scan1 = {1,2,3,4}
scan2 = {3,4,5,6}

scan3 = scan1 & scan2 # output = {3,4}
# hoặc
scan3 = scan1.intersection(scan2)
```
## 5. `Difference` là gì?
ta có:

``` python
scan1 = {1,2,3,4}
scan2 = {3,4,5,6}

print(scan1 - scan2) # output {1,2}
# method
print(scan1.difference(scan2))
```
## 6. duyệt `set`
- `set` không có index nhưng vẫn có thể duyệt = `for`
``` python
scan1 = {1,2,3,4}

for scan in scan1:
	print(scan)
# output
1
2
3
4
```
- có thể kết hợp với `if`
``` python
for port in ports:
    if port > 100:
        print(port)
```
## 7. `list` <-> `set`
### 1. `list` -> `set`
``` python
ports = [22, 80, 443, 80, 22, 8080]
```
- đây là 1 list muốn chuyển thành Set phải dùng type `set`
``` python
list_set = set(ports)

print(list_set) # output = {22,80,443,8080}
```
### 2. `set` -> `list`
- dùng type `list`:
``` python
set_list = list(ports)

print(set_list) # output = [22,80,443]
```
**lưu ý:** không nen dựa vào thứ tự của `set` khi chuyển sang `list`

## 8. `set` comprehension
``` python
numbers = {1, 2, 3, 4, 5}

even = {x for x in numbers if x % 2 == 0}

print(even) # output = {2,4}
```

``` python
{x for x in numbers if x % 2 ==0}
#          | |    
#           V
even = set() # gan even thanh gia tri kieu set()

for x in numbers: # tao vong lap thuc hien cong viec
	if x % 2 ==0: # dieu kien cong viec
		even.add(x) # them gia tri vao even 
```

> `Công thức:` {biểu_thức for biến in collection if điều_kiện}

# TỔNG KẾT
1. `set` là gì? là 1 tập hợp không chứa phần tử trùng nhau, không có index
2. chỉnh sửa `set` = `.add()` (thêm), `.discard()`(xóa nhưng không báo lỗi khi không có giá trị đó) , `.remove()`(xóa nhưng báo lỗi khi không có giá trị để xóa) , cuối cùng là `.update()`(thêm nhiều giá trị cùng 1 lúc)
3. `union` (`|`) lấy tất cả giá trị của 2  `set` , loại trùng
4. `intersection` (`&`) lấy giá trị đã xuất hiện trong 2 `set`, tức là giá trị giống nhau
5. `difference`(`-`) lấy giá trị của `set a` mà không có trong `set b`
6. duyệt `set` = `for` bình thường , mặc dù không có index
7. chuyển đổi `list ` -> `set` = type `set()` và ngược lại là `list()`
8. `set comprehension` giống y chang `list` khác mỗi `{}` cấu trúc: {`biến` for `biến` in `biến kiểu giá trị set` if ....}
9. `{}` đứng 1 mình chưa chắc là 1 set nhưng `set{}` chắc chắn là `set`