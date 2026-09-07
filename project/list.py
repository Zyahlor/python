
## Project: Quản lý danh sách điểm sinh viên

# Viết chương trình quản lý điểm với các chức năng:

# 1. Nhập danh sách điểm (nhập từ bàn phím, cách nhau bởi dấu cách) [x]
# 2. In thống kê: tổng, trung bình, max, min [x]
# 3. Xếp loại: [x]
#    - >= 8.5 → Giỏi
#    - >= 7.0 → Khá
#    - >= 5.0 → Trung bình
#    - < 5.0  → Yếu
# 4. In danh sách điểm đã sắp xếp giảm dần [x]
# 5. Lọc ra danh sách sinh viên Giỏi [x]

# **Yêu cầu bắt buộc dùng:**
# - `input()` để nhập
# - `map()` để chuyển kiểu
# - list comprehension để xếp loại và lọc
# - `sorted()`, `sum()`, `min()`, `max()`

#ý tưởng: tạo 1 biến điểm để input điểm 
# map để chuyển kiểu str -> float từ input 
# thêm .split để nhập 1 số lượng lớn có khoảng cách
# bọc list bên ngoài để thg map ko lười biếng

print("--- quan ly diem sinh vien ---")
diem = list(map(float,input("nhap diem(co the nhap nhieu bang cach cach chung ra):").split()))
print(diem)

#ý tưởng tạo thống kê: gồm có 
# tổng : dùng hàm sum()
# trung bình : sum()/len()
# tìm lớn/nhỏ nhất = max(),min()
print("--- thong ke ---")
print(f"tong diem:{sum(diem)}")
print(f"trung binh:{sum(diem)/len(diem)}")
print(f"diem lon nhat la:{max(diem)}")
print(f"diem nho nhat la:{min(diem)}")

#ý tưởng xếp loại:
# tạo 1 vòng lặp chạy hết cái list điểm
# cho các điều kiên:
#    - >= 8.5 → Giỏi
#    - >= 7.0 → Khá
#    - >= 5.0 → Trung bình
#    - < 5.0  → Yếu

print("--- xet loai ---")
for i in diem:
    if i >= 8.5:
        print(f"{i}:gioi")
    elif i >= 7.0:
        print(f"{i}:kha")
    elif i >= 5.0:
        print(f"{i}:trung binh")
    elif i < 5.:
        print(f"{i}:kem")

#ý tưởng in ds điểm từ cao -> thấp:
# dùng sorted() bọc điểm và thêm reverse True
print(f"mang diem sap xep tu cao den thap la:{sorted(diem,reverse=True)}")

#ý tưởng lọc ra danh sách học sinh giỏi
# dùng list comprehension cho x chạy vòng lặp thêm điều kiện x >=8.5
gioi = [x for x in diem if x >= 8.5]
print(f"cac diem gioi:{gioi}")