# Bài 1: cho a = [5, 3, 8, 1, 9, 2]
# In ra: phần tử đầu, phần tử cuối, 3 phần tử đầu, list đảo ngược
# a = [5, 3, 8, 1, 9, 2]
# print(f"phan tu dau:[{a[0]}]")
# print(f"phan tu cuoi:[{a[-1]}]")
# print(f"3 phan tu dau:{a[:3]}")
# print(f"dao nguoc:{a[::-1]}")

# Bài 2: cho a = [1, 2, 3]
# Thêm 4 vào cuối, chèn 0 vào đầu, nối thêm [5, 6]
# Kết quả mong đợi: [0, 1, 2, 3, 4, 5, 6]
# a = [1, 2, 3]
# print(f"them phan tu vao dau:")
# a.insert(0,0)
# print(a)
#
# b = [5,6]
# a.extend(b)
# print(f"mo rong mang:{a}")

# Bài 3: cho a = [10, 20, 30, 40, 50]
# Xóa 30 (theo giá trị), xóa phần tử cuối (lưu vào biến x), in a và x
# Mong đợi: [10, 20, 40] 50
# a = [10, 20, 30, 40, 50]
# print(a)
# print("xoa phan tu cuoi va luu vao bien:")
# x = a.pop()
# print(f"phan tu moi bi xoa o cuoi:{x}")
# print("xoa theo gia tri:")
# a.remove(30)
# print(a)

# Bài 4: cho a = [4, 7, 1, 9, 3]
# Không dùng sum/max/min, dùng for để tính tổng và tìm số lớn nhất
# a = [4, 7, 1, 9, 3]
# max = a[0]
# sum = a[0]
# for i in range(1,5):
#     if a[i] > max:
#         max = a[i] 
#     sum+=a[i]
# print(f"tong:{sum} | max:{max}")

# Bài 5: đếm bao nhiêu số chẵn trong list
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# dem = 0;
# for i in a:
#     if i % 2 ==0:
#         dem+=1
# print(f"so chan trong mang la:{dem}")

# Bài 6: in ra số lớn nhất VÀ vị trí (index) của nó
# a = [4, 7, 1, 9, 3]
# # TODO  → mong đợi: 9 3
# max = a[0]
# idx = 0
# for i in range(5):
#     if a[i] > max:
#         max = a[i]
#         idx = i
# print(f"so lon nhat:[{max}] | index:[{idx}]")

# Bài 7: cho list số, in ra dạng "1 + 2 + 3 + 4 = 10"
# a = [1, 2, 3, 4]
 # TODO (gợi ý: join + map + sum)
# tong=sum(a)
# x = "+".join(map(str,a)) 
# print(f"{x}={tong}")

# Bài 8: tạo list bình phương của 1..10 bằng 1 dòng
# TODO  → [1, 4, 9, ..., 100]
# b = [1,2,3,4,5,6,7,8,9,10]
# b = [x**2 for x in b ]
# print(b)

# Bài 9: từ list, lấy các số > 5 rồi nhân đôi
# a = [3, 8, 1, 9, 5, 6]
# TODO  → [16, 18, 12]
# b = [x*2 for x in a if x > 5]
# print(b)

# Bài 10: cho list tên, viết hoa chữ cái đầu mỗi tên, bỏ tên rỗng
# names = ["an", "", "binh", "cuong", ""]
# TODO  → ["An", "Binh", "Cuong"]
# new = [x.capitalize() for x in names if x != ""]
# print(new)

# Bài 11: loại phần tử trùng nhưng GIỮ THỨ TỰ ban đầu
# (không dùng set trực tiếp để kết quả)
# ports = [80, 443, 22, 80, 8080, 22, 443]
# # TODO  → [80, 443, 22, 8080]
# new = []
# for i in ports:
#     if i not in new :
#         print(f"[{i}] khong co trong mang new!")
#         new.append(i)
# print(new)

# Bài 12: lọc port "nguy hiểm" ra khỏi danh sách port đang mở
import re


open_ports = [21, 22, 23, 80, 443, 445, 3389, 8080]
risky = [21, 23, 445, 3389]
# TODO  → in ra các port mở mà nằm trong risky: [21, 23, 445, 3389]
# TODO  → in ra các port mở mà KHÔNG nằm trong risky: [22, 80, 443, 8080]
print("lay ra port khong nam trong risky")
new_open_ports = [i for i in open_ports if i not in risky]
print(new_open_ports)

print("lay ra port nam trong risky")
new_risky = [i for i in open_ports if i in risky]
print(new_risky)
# Bài 13: tìm số lớn thứ 2 (không dùng sort/sorted, phải xử lý list có số trùng)
a = [5, 9, 9, 3, 7]
# TODO  → 7
mx = max(a)
reset = [x for x in a if x != mx]
if not reset:
    print("khong co so lon thu 2 trong mang!")
else:
    print(f"so lon thu 2:[{max(reset)}]")
# Bài 14: ghép 2 list thành list các cặp (gợi ý: zip hoặc range(len))
users = ["admin", "root", "guest"]
pwds  = ["123456", "toor", "guest"]
# TODO  → ["admin:123456", "root:toor", "guest:guest"]
new = [f"{i}:{p}" for i,p in zip(users,pwds)]
print(new)

# Bài 15: sinh wordlist nhỏ bằng comprehension
# Từ base = ["admin", "root"] và nums = [1, 2, 3]
# → ["admin1", "admin2", "admin3", "root1", "root2", "root3"]
base = ["admin", "root"]
nums = [1, 2, 3]
# TODO (gợi ý: comprehension 2 vòng for)
new = [f"{i}{n}" for i in base for n in nums]
print(new)
