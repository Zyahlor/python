scan_old = [22, 80, 80, 443, 443, 3306]
scan_new = [22, 80, 443, 8080, 8080, 3306, 3306]

#Loại port trùng.
# Tìm port mới xuất hiện.
# Tìm port biến mất.
# Tìm port tồn tại ở cả hai lần scan.
# Tìm các port >= 1024.
# In kết quả rõ ràng.

# 1 loai port trung
# y tuong dung set cho scan_old/new
scan_new = set(scan_new)
scan_old = set(scan_old)
print(f"scan_new:{scan_new} | scan_old:{scan_old}")

# 2 tim port moi xuat hien
# y tuong dung difference - scan_new dung trc old sau
print(f"port moi xuat hien:{scan_new - scan_old}")

# 3 tim port bien mat
# y tuong dung lai difference nhung cho old dung trc
print(f"port bien mat:{scan_old - scan_new}")

# 4 tim port ton tai ca 2 lan scan
# y tuong dung intersection &
print(f"ports xuat hien ca 2 lan scan:{scan_new&scan_old}")

# 5 tim port >= 1024
# dung set comprehension cho nhanh
lon = {x for x in scan_new if x >= 1024}
print(f"port tim duoc >= 1024:{lon}")

