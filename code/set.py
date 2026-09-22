# ============================================================
# PHÂN LOẠI BÀI TẬP: SET TRONG PYTHON
# ============================================================

# 1. Kiểu bài tập: Khởi tạo, kiểm tra và thao tác cơ bản với set
# # ports = {22, 80, 443, 80, 22, 8080, 443}
# # # xuat set
# # print(ports)

# # print(80 in ports) # true
# # print(3306 in ports) # false
# # # print(ports[0]) loi!
# # ports.add(99)
# # print(ports)

# # ports.update([1,2,3,4,5])
# # print(ports)

# # ports.remove(1)
# # print(ports)


# 2. Kiểu bài tập: Thêm và xóa phần tử trong set
# # ports = {22, 80, 443}
# # # them 53 vao
# # ports.add(53)
# # print(ports)
# # # them cung luc 21,25,110
# # ports.update([21,25,110])
# # print(ports)
# # # xoa port 80
# # ports.remove(80)
# # print(ports)
# # # discard xoa 9999
# # ports.discard(9999)
# # print(ports)


# 3. Kiểu bài tập: Phép toán hợp (union)
# # print('union')
# # scan1 = {1,2,3,4,5}
# # scan2 = {3,4,5,6}
# # scan3 = scan1 | scan2 
# # print(scan3)
# # scan3 = scan1.union(scan3)
# # print(scan3)

# 4. Kiểu bài tập: Phép toán giao (intersection)
# # print('intersection')
# # scan1 = {1,2,3,4,5}
# # scan2 = {3,4,5,6}
# # scan3 = scan1 & scan2
# # print(scan3)

# # scan3 = scan3.intersection(scan1)
# # print(scan3)

# # scan1 = {21, 22, 80, 443}
# # scan2 = {22, 80, 443, 8080, 3306}
# # print(scan1|scan2)
# # print(scan1&scan2)
# # scan1.union(scan2)
# # scan1.intersection(scan2)

# 5. Kiểu bài tập: Phép toán hiệu (difference)
# # scan1 = {1,2,3,4}
# # scan2 = {3,4,5,6}

# # print(scan1 - scan2) # output {1,2}
# # # method
# # print(scan2.difference(scan1))

# # scan1 = {21, 22, 80, 443}
# # scan2 = {22, 80, 443, 8080, 3306}

# # print(f"port chi co o scan1 la:{scan1 - scan2}")
# # print(f"port chi co o scan2 la:{scan2 - scan1}")
# # print("method")
# # print(f"port chi co o scan1 la:{scan1.difference(scan2)}")
# # print(f"port chi co o scan2 la:{scan2.difference(scan1)}")

# 6. Kiểu bài tập: Duyệt các phần tử trong set bằng vòng lặp
# # scan1 = {1,2,3,4}

# # for scan in scan1:
# #     print(scan)

# 7. Kiểu bài tập: Lọc phần tử bằng điều kiện và vòng lặp
# # ports = {21, 22, 53, 80, 443, 3306, 8080}
# # # in toàn bộ port

# # for port in ports:
# #     print(port)
# #     # chỉ in ra port lớn hơn 100
# #     if port > 100:
# #         print(port)
# #     if port % 2 == 0:
# #         print(port)

# 8. Kiểu bài tập: Chuyển đổi giữa list và set, loại bỏ phần tử trùng
# # list -> set
# # ports = [22, 80, 443, 80, 22, 8080]

# # unique_ports = set(ports)

# # print(unique_ports)

# 9. Kiểu bài tập: Bài tập tổng hợp so sánh hai lần quét
# # # bài 1
# # ports = [22, 80, 443, 80, 22, 8080, 443, 3306]
# # new_ports = set(ports)
# # print(new_ports)

# # # bài 2
# # ports = {22, 80, 443, 8080}
# # new_list =  list(ports)
# # print(new_list)
# # print(type(new_list))

# # # bài 3
# # scan_old = [22, 80, 80, 443, 443]
# # scan_new = [22, 80, 443, 8080, 8080, 3306]
# # # chuyen thanh set
# # scan1 = set(scan_old)
# # scan2 = set(scan_new)
# # print(f"scan1:{scan1}")
# # print(f"scan2:{scan2}")

# # # tim port moi xuat hien trong scan moi
# # print(f"port moi phat hien duoc:{scan2-scan1}")

# # # port khong con xuat hien o scan moi
# # print(f"port khong con xuat hien o scan moi:{scan1-scan2}")

# # # port xuat hien o ca 2
# # print(f"port xuat hien o ca 2:{scan1&scan2}")

# 10. Kiểu bài tập: Set comprehension (tạo set theo điều kiện)
# # set comprehension
# ports = {21, 22, 23, 25, 53, 80, 443, 3306}
# chan = {x for x in ports if x % 2 == 0}
# print(chan)

# # tao set chua port lon hon 100
# lon = {x for x in ports if x > 100}
# print(lon)

# # tao set chuaw nhung port thuoc 1024 tro len
# ports = {21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080}
# new_ports = {x for x in ports if x >= 1024}
# print(f"cac ports lon hon 1024:{new_ports}")
