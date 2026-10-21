def tac(line):
    new =  line.split(":")
    return new 
# Bài 1: cho list các tọa độ (x, y)
points = [(1, 2), (3, 4), (5, 6)]
# a) In từng điểm dạng "x=1, y=2" (unpack trong for)
for x,y in points:
    print(f"{x},{y}")
# b) Tạo list chỉ chứa các x: [1, 3, 5]
a=[]
for i,x in points:
    a.append(i)
print(a)
# c) Tạo list tổng x+y mỗi điểm: [3, 7, 11]
b = []
for i,x in points:
    b.append(i+x)
print(b)
# Bài 2: tách list tuple thành 2 list riêng
pairs = [("admin", "123"), ("root", "toor"), ("guest", "guest")]
# TODO → users = ["admin", "root", "guest"]
#        pwds  = ["123", "toor", "guest"]
a=[]
b=[]
for i,x in pairs:
    a.append(i)
    b.append(x)
print(a)
print(b)

# Bài 3: cho kết quả scan, lấy list các (ip, port) của dòng "open"
scan = [
    ("10.0.0.1", 80, "open"),
    ("10.0.0.1", 22, "closed"),
    ("10.0.0.2", 443, "open"),
    ("10.0.0.3", 21, "filtered"),
    ("10.0.0.3", 3389, "open"),
]
# TODO → [("10.0.0.1", 80), ("10.0.0.2", 443), ("10.0.0.3", 3389)]
new =[]
for i,x,z in scan:
    result = (i,x)
    new.append(result)
print(new)
# Bài 4: từ scan ở trên, đếm có bao nhiêu port open, closed, filtered
# (chưa học dict nên dùng 3 biến đếm)
# TODO → open: 3 | closed: 1 | filtered: 1
dem_open =0
dem_closed = 0
dem_fiiltered = 0
for i,x,z in scan:
    if z == 'open':
        dem_open+=1
    elif z == 'closed':
        dem_closed+=1
    else:
        dem_fiiltered+=1
print(f"open:{dem_open} | closed:{dem_closed} | filtered:{dem_fiiltered}")

# Bài 5: tìm tuple có port lớn nhất trong scan
# Không dùng max() với key, dùng for + so sánh
# TODO → ("10.0.0.3", 3389, "open")
mx = scan[0]
for i in scan:
    if mx[1] < i[1]:
         mx = i 
print(mx)

# Bài 6: cho list học sinh (tên, điểm)
students = [("An", 7), ("Binh", 9), ("Cuong", 5), ("Dung", 9)]
# a) In học sinh có điểm cao nhất (xử lý trường hợp trùng điểm: in tất cả)
top = max(diem for ten,diem in students)
mx = [ten for ten,diem in students if diem == top]
print(mx)
# b) Tạo list tên của học sinh điểm >= 7
names = []
for ten,diem in students:
    if diem >= 7:
        names.append(ten)
print(names)
# c) Điểm trung bình (dùng sum + len + comprehension)
tong = [x for i,x in students]
avg = sum(tong) / len(tong)
print(avg)
# TODO


# Bài 7: ghép 2 list thành list tuple, rồi lọc
ips   = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
ports = [80, 22, 443]
# a) Ghép thành [("10.0.0.1", 80), ...] bằng zip
new =[]
for ip,port in zip(ips,ports):
    result = (ip,port)
    new.append(result)
print(new)
# b) Lọc ra các cặp có port < 100
# TODO
x =[]
for i in new:
    if i[1] < 100:
        x.append(i)
print(x)

# Bài 8: loại trùng nhưng giữ thứ tự, với list tuple
targets = [("10.0.0.1", 80), ("10.0.0.2", 22), ("10.0.0.1", 80), ("10.0.0.2", 443)]
# TODO → [("10.0.0.1", 80), ("10.0.0.2", 22), ("10.0.0.2", 443)]
# (giống bài 11 list, nhưng phần tử là tuple)
new = []
for target in targets:
    if target not in new:
        new.append(target)
print(new)

# Bài 9: viết hàm parse_line(line) nhận chuỗi "10.0.0.1:80:open"
# trả về tuple (ip, port, status), trong đó port là int
# Gợi ý duy nhất: str có method .split(":")
# parse_line("10.0.0.1:80:open") → ("10.0.0.1", 80, "open")
# TODO
a = "192.168.1.2:80:open"
new=tac(a)
ip,port,status = new
port= int(port)
a = (ip,port,status)
print(a)

# Bài 10: dùng parse_line cho cả list, rồi lọc open
lines = [
    "10.0.0.1:80:open",
    "10.0.0.1:22:closed",
    "10.0.0.2:443:open",
]
# TODO → in ra: 10.0.0.1:80 và 10.0.0.2:443
# (comprehension + unpacking)
new = []
for line in lines:
    ip,port,status = tac(line)
    port = int(port)
    if status == 'open':
        new.append((ip,port))
print(new)
