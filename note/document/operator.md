# 24 - 08 - 2026
# **OPERATOR**

## 1. toán tử số học

gồm có:
 - `+` : cộng
 - `-` : trừ
 - `*` : nhân
 - `/` : chia này trả về float
 - `//`: chia này trả về số nguyên
 - `%` : chia trả về phần dư
 - `**` : lũy thừa

 ## 2. toán tử so sánh

gồm có :
 - ` == ` : bằng nhau về giá trị
 - ` != ` : khác nhau    
 - ` >,<` : dấu lớn, nhỏ
 - `>=,<=` : lớn hơn hoặc = , nhỏ hơn hoặc bằng

*mẹo*

cho phép viết chuõi so sánh ngắn gọn như toán học: 1 < x  < 10 => 1 < x and x < 10

## 3. toán tử logic


gồm có:
 - `and`: trả về True khi cả hai vế đúng
 - `or` : trả về True khi ít nhất 1 vế đúng, thực hiện từ trái qua phải
 - `not`: phủ đỉnh giá trị not True -> False

## 4. toán tử gán

gồm có:
 - gán cơ bản : =  vd: n = 10 => gán n = 10
 - gán + phép tính : +=,-=,*=,.. có bao nhiêu phép toán làm đc hết
 - walrus operator: vừa gán vừa trả về giá trị biểu thức (:=)
 vd : if(n := len(name)) >0: print(n)

## 5. toán tử nhận dạng
dùng để ktra 2 biến cso cùng trỏ vào 1 vùng bộ nhớ ko,cùng object ko

is = true nếu cùng tham chiếu ô nhớ

is not =  trả về true nếu khác ô nhớ

``` python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True  (Gia tri giong nhau)
print(a is b)  # False (Hai danh sach nam o 2 dia chi o nho khac nhau)
```

## 6. toán tử thành viên
ktra sự tồn tịa của 1 phần tử trong chuỗi,list,dictionary

``` python
in: "admin" in ["user", "guest", "admin"] -> in: "root" 
not in ["user", "guest"] -> True
```

## 7. toán tử trên bit

thao tác trực tiếp các bit nhị phân,thường dùng khi xử lý mạng, mã hóa, phân quyền

gồm có:
- `&`(AND),`|` (OR), `^` (XOR), `~` (NOT đảo bit)
 - `<<` (dịch trái) , `>>` (dịch phải)