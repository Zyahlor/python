scan1 = {22, 80, 443, 8080, 3306, 80}
scan2 = {22, 25, 443, 8080, 5432, 8080}
""" 
Hiển thị danh sách port duy nhất của cả hai lần scan.
Tìm các port xuất hiện trong cả hai lần scan.
Tìm port mới xuất hiện ở scan2 so với scan1.
Lọc các port có số hiệu từ 1024 trở lên bằng set comprehension.
Cho người dùng nhập một port, kiểm tra port đó có xuất hiện trong lần scan thứ hai không.
"""
print(f"scan1:{scan1 - scan2} | scan2:{scan2 - scan1}")
print(f"tat ca cac port xuat hien trong 2 scan :{scan1.intersection(scan2)}")
all_scan = scan1|scan2
x = {x for x in all_scan if x >= 1024}
print(x)
port = int(input("nhap port kiem tra xem co xuat hien o lan scan 2 ko:"))
if port in scan2:
    print(f"[+] {port} co xuat hien o lan scan2")
else:
    print(f"[!] {port} khong xuat hien o lan scan2")

