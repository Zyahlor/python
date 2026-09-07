# 29 - 08 - 2026
# ***LIST**

## 1. list là gì?
- là 1 dãy các phần tử được lưu theo thứ tự, có thể chứa nhiều kiểu dữ liệu khác nhau

- có thể nói đây là mảng của python

- khác vs c/c++ mỗi mảng chỉ lưu được kiểu dữ liệu duy nhất

```python
a = [1,2,4,5,]
b = [1,"g",4,6,3]
```

``` c++
int a[] = {1,2,3,4,5}
char name[] = "hello"
```
### 1.1.1 index
- mỗi phần tử có 1 chỉ số index, bắt đầu từ 0

vd:
```python
a = [1, 2, 3, 4]

a[0]  # → 1
a[1]  # → 2
a[3]  # → 4
# nếu idx âm:
a[-1]  # → 4  (phần tử cuối)
a[-2]  # → 3
```
### 1.1.2 slice
- lấy 1 đoạn thay vì 1 phần tử từ list
> cú pháp: a[start:stop]

> lấy từ  idx thứ 0 -> stop n-1, không bao gồm stop

- có thể **bỏ** stop hay start đều đc, thậm chí có thể bỏ cả 2 , bỏ cả 2 = copy lại cả list đó

### 1.1.3 duyệt list
- dùng for để đi hết tất cả các phần tử trong list
```python
a = [1,2,3,4]
for idx in a:
    print(x)
    # idx = 0 => 1
    # idx = 1 => 2
    # idx = 2 => 3
    # idx = 3 => 4
```
- **khác biệt** giữa print(a) và dùng for để duyệt

dùng print(a) = xuất cả mảng, không đi từng phần tử, không thể bốc phần tử mình cần ra

dùng for có thể bốc phần tử mình cần ra để xử lý công việc
```python
a = [1,2,3,4,5]

print(a) # [1,2,3,4,5]

for idx in a:
    print(idx)
    # idx  => 1
    # idx  => 2
    # idx  => 3
    # idx  => 4
    # idx  => 5
```
### 1.2 thêm/xóa/sửa/chèn phần tử
1. `.append()`
- thêm phần tử vào cuối list

vd:
```python
a = [1, 2, 3]
a.append(4)
print(a)  # → [1, 2, 3, 4]
```
2. `.insert()`
- thêm vào vị trí bất kỳ
``` python
a = [1, 2, 3]
a.insert(1, 99)
print(a)  # → [1, 99, 2, 3]
```
> cú pháp: a.insert(idx,value) => idx = vị trí phần tử, value là giá trị cần thêm
3. `.extend()`
- nối 1 list khác vào cuối
``` python
a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)  # → [1, 2, 3, 4, 5]
```
- sự **khác** nhau giữa .append() và .extend()

nếu thêm = append() thì sẽ sinh ra hiện tượng là list lồng list
``` python
a.append(b)
print(a)  # → [1, 2, 3, [4, 5]]  ← list lồng list
```
nhưng vs extend() thì khác, nó thêm phần tử của list đó vào list cần thêm
``` python
a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)  # → [1, 2, 3, 4, 5]
```
4. `.pop()`
- xóa phần tử theo index,mặc định xóa phần tử cuối
``` python
a = [1, 2, 3, 4]
a.pop()     # xóa cuối
print(a)    # → [1, 2, 3]

a.pop(1)    # xóa index 1
print(a)    # → [1, 3]
```
- còn trả về phần tử đã xóa
``` python
x = a.pop()
print(x)    # → giá trị vừa bị xóa
```

5. `.remove()`
- xóa theo giá trị
``` python
a = [1, 2, 3, 4]
a.remove(3)
print(a)    # → [1, 2, 4]
```
- sẽ báo lỗi nếu ko có giá trị
``` python
a.remove(99)  # → ValueError
```
6. `del`
- xóa theo index, có thể xóa cả list
``` python
a = [1, 2, 3, 4]
del a[1]
print(a)    # → [1, 3, 4]

del a       # xóa luôn cả list
```
### 1.3 find
- dùng in để kiểm tra phần tử có trong list hay không
``` python
a = [1, 2, 3, 4]

3 in a   # → True
9 in a   # → False
```
``` python
if 3 in a:
    print("có")
else:
    print("không có")
```
- muốn tìm vị trí của phần tử, sài `.index()`
``` python
a = [1, 2, 3, 4]
a.index(3)   # → 2
```

### 1.4 hàm thường dùng
1. `len()`
- dùng để đếm phần tử trong list

```python
a=[1,2,3,4,5]
print(len(a)) # => 5
```
- sự khác nhau giữa len(str) và len(list)

len(str) = đếm các ký tự của 1 chuỗi

len(list)= đếm các phần tử của 1 list

```python
a=["hello","world"]
b="hello world"

print(len(a))# => 2 vì trong list chỉ có 2 phần tử là "hello" và "world"
print(len(b))# => 11 vì đó là ký tự trong 1 chuỗi, khoảng chắn cx là 1 ký tự 
```
2. `sum()`
- tính tổng các phần tử
``` python
a = [1, 2, 3, 4]
sum(a)   # → 10
```
3. `max()/min()`
- tìm giá trị lớn nhất, nhỏ nhất trong list
``` python
a = [3, 1, 4, 1, 5]
max(a)   # → 5
min(a)   # → 1
```
4. `sorted()`
- sắp xếp mà không thay đổi list gốc
``` python
a = [3, 1, 4, 1, 5]
b = sorted(a)
print(b)   # → [1, 1, 3, 4, 5]
print(a)   # → [3, 1, 4, 1, 5]  ← không đổi
```
- **giảm dần**
``` python
sorted(a, reverse=True)   # → [5, 4, 3, 1, 1]
```

- **khác biệt** giữa `.sort()` và `.sorted()`
sorted() không thay đổi list gốc và trả về list mới, còn .sort() thay đổi list gốc
5. `join()`
- nối các phần tử thành 1 chuỗi
``` python
a = ["hello", "world", "python"]
print(" ".join(a))   # → hello world python
print("-".join(a))   # → hello-world-python
print("".join(a))    # → helloworldpython
```

**chú ý:**
- join chỉ nối đc string,list là số thì phải chuyển sang str
``` python
a=[1,2,3,4]
print("-".join(a)) #typeError

print("-".join(map(str,a))) # 1-2-3-4
```

**kiến thức ngoài lề:**
- `map()` dùng đề chuyển đổi kiểu dữ liệu của list 
vd:
``` python
a = ["1", "2", "3"] # int
b = list(map(int, a))
print(b)   # → [1, 2, 3]
```
>map() không xử lý ngay toàn bộ list — nó chỉ ghi nhớ "sẽ làm gì", xử lý từng phần tử khi nào cần.

``` python
a = ["1", "2", "3"]
m = map(int, a)   # chưa chuyển gì cả, chỉ ghi nhớ "sẽ chuyển int"
list(m)   # lúc này mới chuyển → [1, 2, 3]
```
### 1.5 list comprehension
- các viết ngắn gọn để tạo list mới từ list có sẵn

cách thường:
``` python
a = [1, 2, 3, 4, 5]
b = []
for x in a:
    b.append(x * 2)
print(b)  # → [2, 4, 6, 8, 10]
```

dùng list comprehension:

``` python
a = [1, 2, 3, 4, 5]
b = [x * 2 for x in a]
print(b)  # → [2, 4, 6, 8, 10]
```

> [biểu_thức for biến in list]

thêm điều kiện:
``` python
a = [1, 2, 3, 4, 5, 6]
b = [x for x in a if x % 2 == 0]
print(b)  # → [2, 4, 6]
```
> [biểu_thức for biến in list if điều_kiện]
