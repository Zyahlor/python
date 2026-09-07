# 24-08-2026
# **LOOP**

## 1. loop là gì
vòng lặp loop cho phép lặp lại công việc nhiều lần mà không cần phỉa viết nhiều đoạn mã công việc đó

khác vs c++, python chỉ có 2 vòng lặp là while và for

while giống c++, phải có điều kiện làm mốc để thực hiền công việc nằm ở bên trong

for thì lại khác, for của c++ phải bao gôm 3 mệnh đề tham số:
 - gán giá trị cho biến đếm
 - điều kiên dừng lặp
 - tăng giá trị của biến đếm
 
có 1 loại là for thiếu, không cần đầy đủ 3 tham số đó vẫn hoạt động

for của python hoạt đông theo cơ chế `for - each` duyệt trực tiếp từng phần tử của đối tượng

## 2. range()
hàm range() thuộc for, cấu trúc của nó bao gồm:
range(start,stop,step)

vd:
``` python
for i in range (1,10,1):
    print(i)
```
- start: số bắt đầu, mặc định = 0
- stop: điểm kết thúc,không bao gồm giá trị đặt  vd: range(1,10,1) => stop = 10 thì chỉ chạy từ 1 -> 9
- step: bước nhảy,có thể âm, mặc định là 1

## 3. các kiểu duyệt của for
### 1. các kiểu duyệt
- duyệt vs giá trị là số nguyên:
``` python
for i in range (1,10,1):
    print(i)
```

- duyệt chuỗi
``` python
for i in 'python':
    print(i)
```

- duyệt list

``` python
a = [1,2,3,54,6]
for i in a :
    print(i)
```

- duyệt dictionary
``` python
info = {"name": "bao", "age":20,"school":"cao thang"}
for i,value in info.items():
    print(f"infomation:{i} -> values:{value}" )
```

### 2. các hàm bổ trợ
`enumerate()` & `zip()`

1. `enumerate()`

vừa lấy chỉ số index, vừa lấy giá trị

```python
targets = ["192.168.1.1", "192.168.1.254", "10.0.0.1"]
for idx, ip in enumerate(targets, start=1):
    print(f"Target #{idx}: {ip}")
```
2. `zip()`
ghép và  duyệt song song nhiều mảng khác nhau

```python
hosts = ["web_srv", "db_srv", "mail_srv"]
ips = ["10.0.0.10", "10.0.0.20", "10.0.0.30"]
for host, ip in zip(hosts, ips):
    print(f"Host: {host} có IP: {ip}")
```

| Lệnh | Mô tả |
|---|---|
| `break` | Ngắt và thoát ngay lập tức khỏi vòng lặp hiện tại |
| `continue` | Bỏ qua phần còn lại của vòng lặp hiện tại và nhảy sang lần lặp tiếp theo |
| `pass` | Câu lệnh giữ chỗ (placeholder), không thực hiện hành động nào |

```python
for port in range(1, 1024):
    if port == 80:
        pass  # TODO: Se viet code scan HTTP sau
```
3. Cấu trúc `else` trong vòng lặp (Đặc trưng của Python)

Khối lệnh `else` đi kèm `for` hoặc `while` sẽ được thực thi **khi và chỉ khi** vòng lặp kết thúc bình thường (không bị ngắt bởi câu lệnh `break`).

```python
# Vi du: Tim kiem so nguyen to
num = 29
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print(f"{num} chia het cho {i} -> Khong phai so nguyen to")
        break
else:
    # Chi chay khi khong co break nao duoc kich hoat
    print(f"{num} la so nguyen to!")
```

# Phân biệt 3 cách duyệt mảng trong Python
---

## Tổng quan nhanh

| Cách | Cú pháp | Lấy được gì | Dùng khi nào |
|---|---|---|---|
| `for i in arr` | `for item in arr` | **Giá trị** trực tiếp | Chỉ cần giá trị, không cần index |
| `arr[i]` | `arr[0]`, `arr[n]` | **Giá trị** tại index i | Cần truy cập theo vị trí cụ thể |
| `==` | `item == target` | So sánh **True/False** | Kiểm tra phần tử có bằng giá trị không |

---

## 1. `for i in arr` — Duyệt trực tiếp lấy giá trị

```python
arr = ["ftp", "ssh", "http"]

for item in arr:
    print(item)
# Output:
# ftp
# ssh
# http
```

- `item` = **giá trị** của từng phần tử
- Không biết index là bao nhiêu
- Dùng khi **chỉ cần giá trị**

---

## 2. `arr[i]` — Truy cập theo index

```python
arr = ["ftp", "ssh", "http"]

print(arr[0])   # ftp
print(arr[1])   # ssh
print(arr[2])   # http
```

- `i` = số thứ tự vị trí (bắt đầu từ 0)
- Dùng khi cần **truy cập vị trí cụ thể**
- Thường dùng với `while`:

```python
n = 0
while n < len(arr):
    print(arr[n])   # lấy từng phần tử theo index
    n += 1
```

---

## 3. `==` vs `in` — So sánh phần tử

### `==` So sánh 1 giá trị với 1 giá trị
```python
item = "ssh"
if item == "ssh":       # ✅ True
    print("found!")

if item == ["ssh"]:     # ❌ False — so sánh string với list
    print("found!")
```

### `in` Kiểm tra phần tử có nằm trong list không
```python
item = "ftp"
dangerous = ["ftp", "telnet", "rdp"]

if item in dangerous:   # ✅ True — tìm trong list
    print("dangerous!")

if item == dangerous:   # ❌ sai — so sánh string với cả list
    print("dangerous!")
```

---

## Bảng lỗi hay gặp

| ❌ Sai | ✅ Đúng | Lý do |
|---|---|---|
| `if item == arr` | `if item in arr` | So sánh string với list |
| `if target in arr` trong for | `if item == target` | Kiểm tra cả list thay vì từng phần tử |
| `arr[i]` khi dùng `for item in arr` | Dùng `item` trực tiếp | `for in` đã lấy giá trị rồi |
| `while n <= len(arr)` | `while n < len(arr)` | Index cuối là `len-1`, `<=` gây lỗi out of range |

---

## Ví dụ tổng hợp — Port Scanner

```python
ports = [22, 23, 80, 443]
dangerous = [23, 21]
target = 80

# for in → lấy giá trị trực tiếp
for port in ports:

    # == → so sánh 1 vs 1
    if port == target:
        print(f"Target port {port} found!")

    # in → kiểm tra có trong list không
    if port in dangerous:
        print(f"Port {port} is DANGEROUS!")
```

---

## Khi nào dùng cái nào?

```
Chỉ cần giá trị          → for item in arr
Cần index + giá trị      → enumerate(arr)
Cần index, dùng while    → arr[n] với biến đếm n
So sánh 1 phần tử        → item == target
Tìm trong list           → item in list
```