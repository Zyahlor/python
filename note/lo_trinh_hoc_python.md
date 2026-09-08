# 🐍 Lộ trình học Python

> Mục tiêu: học Python theo hướng **thực hành**, lý thuyết ngắn gọn nhưng phải hiểu bản chất.  
> Định hướng: lập trình nền tảng → scripting → networking → pentest/cybersecurity.

---

# 0. Cách học

Mỗi chủ đề đi theo thứ tự:

1. Hiểu khái niệm
2. Xem 1–2 ví dụ
3. Tự code lại, không copy
4. Làm bài tập
5. Sửa lỗi
6. Làm mini project

**Nguyên tắc:** Không học cú pháp để thuộc lòng. Học để biết **tại sao nó hoạt động**.

---

# 1. Python cơ bản

## 1.1 Biến và kiểu dữ liệu [X]
- `int`
- `float`
- `str`
- `bool`
- Gán biến
- Ép kiểu: `int()`, `float()`, `str()`

## 1.2 Input / Output [X]
- `input()`
- `print()`
- f-string

## 1.3 Toán tử [X]
- `+ - * /`
- `// % **`
- `== != > < >= <=`
- `and`, `or`, `not`

## 1.4 Điều kiện [x]
- `if`
- `elif`
- `else`

## 1.5 Vòng lặp[x]
- `for`
- `while`
- `range()`
- `break`
- `continue`

### Bài tập  [x]
- Kiểm tra chẵn/lẻ
- Tìm max/min
- Tính tổng
- Đếm số
- Kiểm tra số nguyên tố
- Bảng cửu chương

---

# 2. String

## Học
- `Index`     [x]
- `Slice`     [x]
- `len()`     [x]
- `.lower()`  [x]
- `.upper()`  [x]
- `.strip()`  [x]
- `.split()`  [x]
- `.replace()`[x]
- `.find()`   [x]
- `.join()`   [x]

### Quan trọng

```python
" ".join(["hello", "world"])
```

`join()` lấy các string và nối chúng bằng chuỗi đứng trước `.join()`.

### Bài tập [x]
- Đếm ký tự
- Đếm từ
- Kiểm tra palindrome
- Chuẩn hóa chuỗi
- Tách họ tên

---

# list [x]

## 3.1 Cơ bản [x]
```python
a = [1, 2, 3, 4]
```

- Index
- Slice
- Duyệt list

## 3.2 Thêm / xóa [x]
- `.append()`
- `.insert()`
- `.extend()`
- `.pop()`
- `.remove()`
- `del`

## 3.3 Tìm kiếm
```python
x in a
```

## 3.4 Hàm thường dùng [x]
- `len()`
- `sum()`
- `max()`
- `min()`
- `sorted()`

## 3.5 `enumerate()`[x]

```python
for i, x in enumerate(a):
    print(i, x)
```

Dùng khi cần **cả index và value**.

## 3.6 `join()` [x]

```python
print("-".join(map(str, a)))
```

`join()` chỉ nối string, vì vậy số cần được chuyển thành string.

## 3.7 List comprehension ⭐⭐⭐ [x]

```python
[x for x in a if x % 2 == 0]
```

Tương đương:

```python
b = []

for x in a:
    if x % 2 == 0:
        b.append(x)
```

### Bài tập [x]
- Nhập list
- Tính tổng
- Đếm chẵn/lẻ
- Tìm max/min
- Tìm kiếm
- Xóa phần tử
- Đảo list
- Tìm số lớn thứ hai
- Lọc số nguyên tố
- Sort thủ công

---

# 4. Tuple

```python
a = (1, 2, 3)
```

## Index [x]
```python
a[0]     # 1
a[-1]    # 3
```

## Slice [x]
```python
a[0:2]   # (1, 2)
a[::-1]  # (3, 2, 1) — đảo ngược
```

## Duyệt
```python
for x in a:
    print(x)

for i, x in enumerate(a):
    print(i, x)
```

## Unpacking
```python
x, y, z = a
x, *rest = a      # x=1, rest=[2,3]
a1, (b, c) = (1, (2, 3))   # nested unpacking → a1=1, b=2, c=3
```

## Khác biệt giữa `list` và `tuple`
| | Tuple | List |
|---|---|---|
| Đổi được | ❌ | ✅ |
| Hashable (làm dict key) | ✅ | ❌ |

## Tuple methods (chỉ có 2)
```python
a.count(2)   # 1 — đếm số lần xuất hiện
a.index(3)   # 2 — vị trí đầu tiên tìm thấy
```

## ⚠️ Immutable nhưng chứa mutable bên trong
```python
t = (1, [2, 3])
t[1].append(4)   # ✅ chạy được! list bên trong vẫn đổi được
t          # (1, [2, 3, 4])
# t[0] = 99  ❌ lỗi — chỉ phần tử gốc của tuple là bất biến
```

## Tuple 1 phần tử
```python
x = (5,)    # ✅ tuple
y = (5)     # ❌ int, không phải tuple
```

## `tuple()` constructor
```python
tuple([1, 2, 3])   # (1, 2, 3)
tuple("abc")       # ('a', 'b', 'c')
```

### Hiểu bản chất

`list` có thể thay đổi.

`tuple` không thể thay đổi sau khi tạo.

---

# 5. Set

```python
a = {1, 2, 3}
```

Học:
- Không chứa phần tử trùng
- Thêm/xóa
- `in`
- Union
- Intersection
- Difference

### Bài tập
- Xóa phần tử trùng trong list
- Tìm phần tử chung giữa hai list
- Tìm phần tử chỉ xuất hiện ở một list

---

# 6. Dictionary ⭐⭐⭐

```python
user = {
    "name": "Bao",
    "age": 19
}
```

Học:
- Key / Value
- Truy cập
- Thêm
- Sửa
- Xóa
- `.keys()`
- `.values()`
- `.items()`
- `.get()`

### Quan trọng

```python
for key, value in user.items():
    print(key, value)
```

### Bài tập
- Quản lý sinh viên
- Đếm tần suất xuất hiện của ký tự
- Đếm số lần xuất hiện của phần tử trong list
- Mini database bằng dictionary

---

# 7. Function ⭐⭐⭐

## Học
- `def`
- Parameter
- Argument
- `return`
- Scope
- Default argument
- Keyword argument

Ví dụ:

```python
def tong(a, b):
    return a + b
```

### Bài tập
Viết function:
- `is_even()`
- `is_prime()`
- `find_max()`
- `find_min()`
- `count_even()`
- `reverse_list()`

---

# 8. File I/O

## Học
- `open()`
- `read()`
- `readline()`
- `readlines()`
- `write()`
- `with open(...)`

Ví dụ:

```python
with open("data.txt", "r") as f:
    data = f.read()
```

### Bài tập
- Đọc file
- Ghi file
- Đếm số dòng
- Tìm kiếm từ trong file
- Parse log file

---

# 9. Exception Handling

Học:

```python
try:
    ...
except:
    ...
finally:
    ...
```

Các lỗi cần hiểu:
- `ValueError`
- `TypeError`
- `IndexError`
- `KeyError`
- `FileNotFoundError`

### Mục tiêu

Không chỉ biết "lỗi", mà phải biết **Python báo lỗi gì và tại sao**.

---

# 10. Module & Package

Học:

```python
import math
from math import sqrt
```

- Module
- Package
- `pip`
- Virtual environment
- `venv`

---

# 11. OOP

## Học theo thứ tự
1. Class
2. Object
3. Attribute
4. Method
5. `__init__`
6. `self`
7. Encapsulation
8. Inheritance
9. Polymorphism

Ví dụ:

```python
class User:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello {self.name}")
```

### Không cần học OOP quá sớm

Chỉ học sâu khi đã viết được chương trình procedural tương đối thoải mái.

---

# 12. Python nâng cao

## Syntax / Pythonic
- List comprehension
- Dictionary comprehension
- Set comprehension
- Lambda
- `map()`
- `filter()`
- `zip()`
- `enumerate()`
- `sorted(key=...)`

## Iterator / Generator
- Iterable
- Iterator
- `yield`
- Generator expression

## Decorator
- Function decorator
- `@decorator`

## Context Manager
- `with`

---

# 13. Làm việc với dữ liệu

Học:
- JSON
- CSV
- Regex
- Parsing
- Encoding

Đặc biệt:

```python
import json
```

và:

```python
import re
```

### Project
- Log analyzer
- JSON parser
- CSV analyzer

---

# 14. Networking với Python ⭐⭐⭐

Đây là phần quan trọng cho hướng Network Administration / Pentest.

## Học
- `socket`
- TCP
- UDP
- Client / Server
- IP / Port
- DNS
- HTTP

Ví dụ thư viện:

```python
import socket
```

### Project
- TCP client
- TCP server
- Port scanner đơn giản
- DNS lookup tool
- Banner grabber
- Network information tool

---

# 15. HTTP & Web

Học:
- HTTP request/response
- GET
- POST
- Header
- Cookie
- Session
- Status code
- JSON API

Thư viện:
- `requests`

### Project
- HTTP client
- API client
- Website status checker
- Header analyzer
- Simple crawler

---

# 16. Python cho Pentest 🔥

Sau khi nền tảng đủ chắc:

## Công cụ / thư viện
- `requests`
- `socket`
- `scapy`
- `subprocess`
- `os`
- `sys`
- `argparse`
- `re`
- `json`

## Project
1. Port scanner
2. Banner grabber
3. Directory checker
4. HTTP header scanner
5. Subdomain checker
6. Log analyzer
7. Simple network scanner

> Chỉ thực hành trên máy/lab/hệ thống được phép kiểm thử.

---

# 17. Automation / System

Học:
- `os`
- `pathlib`
- `shutil`
- `subprocess`
- `sys`
- `argparse`

### Project
- File organizer
- Backup script
- Log cleanup
- System information collector
- Command automation tool

---

# 18. Async & Concurrency

Sau khi Python cơ bản chắc:

- `threading`
- `multiprocessing`
- `asyncio`
- `async`
- `await`

### Project
- Concurrent port checker
- Async HTTP checker
- Multi-target scanner trong lab

---

# 19. Testing & Debugging

Học:
- Debugger
- `assert`
- `unittest`
- `pytest`
- Logging

Mục tiêu:

**Không chỉ viết code chạy được, mà biết kiểm tra code có đúng không.**

---

# 20. Git + Python Project

Học:
- Git cơ bản
- `.gitignore`
- `requirements.txt`
- `README.md`
- Project structure
- Virtual environment

Cấu trúc mẫu:

```text
project/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── main.py
└── tests/
```

---

# 🧪 Hệ thống Project

## Level 1 — Beginner
- Calculator
- Number checker
- Todo CLI
- Student manager

## Level 2 — Intermediate
- File organizer
- Log analyzer
- Password generator
- JSON/CSV manager

## Level 3 — Networking
- TCP client/server
- Port scanner
- DNS lookup
- HTTP checker

## Level 4 — Pentest
- Banner grabber
- Directory checker
- Subdomain checker
- HTTP security header checker
- Network scanner

## Level 5 — Advanced
- Async scanner
- Multi-threaded crawler
- Modular security toolkit

---

# 🎯 Thứ tự học đề xuất

```text
Python syntax
    ↓
String
    ↓
List
    ↓
Tuple / Set / Dictionary
    ↓
Function
    ↓
File I/O
    ↓
Exception
    ↓
Module / Package / venv
    ↓
OOP
    ↓
JSON / CSV / Regex
    ↓
OS / subprocess
    ↓
Socket
    ↓
HTTP / Requests
    ↓
Scapy
    ↓
Async / Threading
    ↓
Pentest Projects
```

---

# 🧠 Mốc kiểm tra năng lực

## Mốc 1
Có thể tự viết chương trình bằng:
- biến
- if
- loop
- list
- string

## Mốc 2
Có thể:
- chia chương trình thành function
- đọc/ghi file
- xử lý exception
- dùng dictionary

## Mốc 3
Có thể tự làm CLI tool.

## Mốc 4
Có thể:
- làm việc với socket
- HTTP
- JSON
- API
- subprocess

## Mốc 5
Có thể tự xây một tool pentest nhỏ từ đầu mà **không cần AI viết toàn bộ code**.

---

# ⚠️ Quy tắc học với AI

AI chỉ nên đóng vai:

- giải thích khái niệm
- review code
- tìm bug
- gợi ý hướng giải quyết
- giải thích error

Không nên:

```text
"Viết cho tôi project X hoàn chỉnh"
→ copy
→ chạy
→ không hiểu
→ project nằm trong ổ cứng
→ linh hồn bay khỏi cơ thể
```

Thay vào đó:

```text
Tự viết
↓
Chạy
↓
Lỗi
↓
Tự debug
↓
Hỏi AI phần không hiểu
↓
Sửa
↓
Viết lại từ đầu
```

Đây mới là cách biến Python thành **kỹ năng**, thay vì biến ChatGPT thành bộ não thuê ngoài.
