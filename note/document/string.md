# 26 - 08 - 2026
# **string**

## 1. string là gì?
- là chuỗi ký tự được lưu trong bộ nhớ
- String sau khi tạo ra thì cố định hoàn toàn — không sửa được bất kỳ ký tự nào.

vd:
```python
s ='hello'
```

```
H | e | l | l | o
0   1   2   3   4
```

## 2. sự khác biệt giữa chuỗi của python và c++:
1. kiểu:

c++:
- kiểu: std::string or char[](type - c)
- khai báo: string s = "hello";
- độ dài: tự quản (với char[])
- inmutable(bất biến): không
- null - terminated(kết thúc = ký tụ null) : có char[] có \0

python:
- kiểu: object(str)
- khai báo: s = "hello"
- độ dài: tự động
- immutable: có
- null - terminated: không

## 3. cách duyệt index:
```
s = "hello"
```
```
s[0] = 'h'
s[-1] = 'o'
```
> -> h ở vị trí 0, nói cách khác `string` ****giống**** `arr`,`list` nhưng ko thể thay đổi,chỉnh sửa phần tử ở trong nó

> -> có thể ****âm**** và lấy phần tử ****cuối****

## 4. slice(cắt):
- được dùng khi cần lấy phần tử của chuỗi

> Cú pháp: `s[start:stop]` — lấy từ ****start**** đến trước ****stop****

vd:
```python
s = "H e l l o"
#    0 1 2 3 4
```

```python
s[1:4]   # 'ell' -> bỏ phần tử s[0] và s[4]
s[0:3]   # 'Hel'
s[:3]    # 'Hel'  — bỏ start mặc định là 0
s[2:]    # 'llo'  — bỏ stop mặc định là lấy hết phần stop
s[:]     # 'Hello' — copy toàn bộ
```

**step**:

```python
s[::2]   # 'Hlo'  — cách 2 ký tự
s[::-1]  # 'olleH' — đảo ngược
```

>Cú pháp đầy đủ: `s[start:stop:step]`

## 5. các hàm dùng cho chuỗi:
1. len():
- dùng để đếm ký tự của chuỗi

> cú pháp: `len(s)`

vd:
```
s = "Hello"
len(s)  # 5

len("hello world")  # 11 (có space)
len("")             # 0
len("hi\n")        # 3 (\n tính 1 ký tự)
```

2. `.lower()` `.upper()`:
- `.lower()`: dùng để viét thường các chữ cái hoa
- `.upper()`: viết hoa các chữ cái thường

vd:
```python
s = "Hello World"
s.lower()  # "hello world"
s.upper()  # "HELLO WORLD"
```
``` python
input = "Admin"
if input.lower() == "admin":  # ✅ luôn đúng dù gõ hoa thường
    print("ok")
```

3. `.strip`
- xóa khoảng trắng ở đầu và cuối chuỗi

```python
b = "   Le dinh Bao  "
print(f"{b.strip()}") # "Le dinh Bao"
print(b)              #"   Le dinh Bao   " 
```

4. `.split`
- tách string thành list dựa theo separator(toán tử)

vd:
```python
s = "hello world"
s.split()      # ["hello", "world"] — mặc định tách theo space

s = "192.168.1.1"
s.split(".")   # ["192", "168", "1", "1"]

s = "a,b,c"
s.split(",")   # ["a", "b", "c"]

```
5. `replace()`
- dùng để thay đổi chuỗi
- cú pháp:
> string.replace(old,new)

```python
s = "hello world"
s.replace("world", "python")  # "hello python"
```
6. `find()`
- tìm index đầu tiên của chuỗi con

``` python
s ='hello'
h e l l o
0 1 2 3 4

s.find('l') # 2 
s.find('ll') # 2 vì 'l' nó là substring đầu tiên và ở vtri 2
```
7. `.join()`
- nối các phần tử trong list thành string
> cú pháp: "ký_tự_nối".join(list)
``` python
words = ["hello", "world"]
" ".join(words)   # "hello world"
"-".join(words)   # "hello-world"
"".join(words)    # "helloworld"
```