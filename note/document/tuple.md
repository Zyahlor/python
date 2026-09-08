# 07-09-2026
# **TUPLE**

## `TUPLE` là gì?
- là kiểu dữ liệu trong python dùng để lưu nhóm giá trị trong 1 biến duy nhất
- tương tự như list **nhưng** nó lại có tính bất biến
- khai báo khác với list, list dùng [], tuple dùng ()
> bất biến: không thể sửa,thêm,xóa sau khi đã tạo

``` python
a = (1,2,3)
print(type(a)) # => <class 'tuple'>
```

- **đặc điểm chính:**
+ có thứ tự -  vị trí idx cố định, truy cập = a[0], a[1]
+ cho phép trùng giá trị (1,1,2)
+ bất biến - không thêm,sửa,xóa dữ liệu
+ chứa nhiều kiểu dữ liệu như list
+ hashable = có thể tính ra 1 giá trị băm cố định,dùng để tra cứu nhanh trong dict/set

- khi nào **nên dùng** tuple?
+ dữ liệu cố định, không đổi vd: toạn độ,ngày tháng
+ dùng làm key trong dict
+ return nhiểu giá trị từ 1 hàm
``` python
def get_port_status():
    return "10.0.0.1", 80, "open"   # thực chất trả về 1 tuple

result = get_port_status()
print(result)   # ('10.0.0.1', 80, 'open')
```

## index(truy cập vị trí)
- mỗi phần tử trong tuple có 1 index cố định, bắt đầu từ 0 như list, array c/c++
``` python
a = (10, 20, 30, 40, 50)
#     0   1   2   3   4   ← index dương
#    -5  -4  -3  -2  -1   ← index âm

Index dương — đếm từ trái sang
a[0]    # 10 (phần tử đầu tiên)
a[2]    # 30
a[4]    # 50 (phần tử cuối)

Index âm — đếm từ phải sang
a[-1]   # 50 (phần tử cuối cùng)
a[-2]   # 40
a[-5]   # 10 (phần tử đầu, tính ngược)
```
**các lỗi thường gặp:**
``` python
❌ Lỗi thường gặp: IndexError
a = (10, 20, 30)
a[5]    # ❌ IndexError: tuple index out of range

❌ Không gán được qua index
a[0] = 99   # ❌ TypeError: 'tuple' object does not support item assignment
```
- index với tuple lồng nhau:
``` python
t = (1, (2, 3), 4)
t[1]        # (2, 3)  — lấy cả tuple con
t[1][0]     # 2       — lấy phần tử bên trong tuple con
```
vd thực tế:
``` python
result = ("10.0.0.1", 80, "open")
ip = result[0]       # "10.0.0.1"
port = result[1]     # 80
status = result[2]   # "open"
```
## slice 
-  giống như list, cùng cú pháp
>[start:stop:step]
``` python
a = (10, 20, 30, 40, 50)

a[1:3]     # (20, 30)     — index 1 đến trước 3
a[:3]      # (10, 20, 30) — từ đầu đến trước 3
a[2:]      # (30, 40, 50) — từ 2 đến hết
a[:]       # (10, 20, 30, 40, 50) — copy toàn bộ

a[::2]     # (10, 30, 50) — step 2, cách 1 lấy 1
a[::-1]    # (50, 40, 30, 20, 10) — đảo ngược
a[::-2]    # (50, 30, 10) — đảo ngược + step 2

a[1:4:2]   # (20, 40) — từ 1 đến trước 4, step 2
```
- **điểm quan trọng:**
+ slice luôn trả về tuple mới
+ không lỗi khi out - of - range, tự căts vừa đủ
+ số âm tính từ cuối lên
